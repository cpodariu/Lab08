import operator
from copy import deepcopy

from domain.Activity import Activity
from validators.ActivityValidator import ActivityValidator


class ActivityController:
    def __init__(self, repo, person_repo):
        self.__repo = repo
        self.__person_repo = person_repo
        self.__validator = ActivityValidator
        self.__undo = []
        self.__undoable_operations = 0

    def copy_repo(self):
        """Creates a copy of the repository and stores it"""
        if self.__undoable_operations == 0:
            self.__undo = [deepcopy(self.__repo)]
            self.__undoable_operations += 1
        else:
            self.__undo = self.__undo[:self.__undoable_operations]
            self.__undo.append(deepcopy(self.__repo))
            self.__undoable_operations += 1

    def undo_operation(self):
        """Move the previous made copy of the repository into the current repository"""
        if self.__undoable_operations != 0:
            if len(self.__undo) == self.__undoable_operations:
                self.__undoable_operations -= 2
            else:
                self.__undoable_operations -= 1
            self.__repo = self.__undo[self.__undoable_operations]

    def redo_operation(self):
        """Redo an operation, where possible"""
        if self.__undoable_operations < len(self.__undo):
            self.__undoable_operations += 1
            self.__repo = self.__undo[self.__undoable_operations]

    def save(self, id, appointments, date, time, description):
        """Creates a new activity and adds it to the repository

        Arguments:
            entity_id - int
            person_ids - list
            date - int
            time - int
            description - str
        """

        a = Activity(id, appointments, date, time, description)
        self.__validator.validate(a)
        self.__validator.activity_ids_validate(appointments, self.__person_repo.get_all_ids())
        self.__validator.activity_date_validate(date, time, self.__repo.get_all())
        self.__repo + a

    def removeActivity(self, id, person_ids, date, time, description):
        """Removes an activity from the list

        Arguments:
            entity_id - int
            person_ids - list
            date - int
            time - int
            description - str
        """
        a = Activity(id, person_ids, date, time, description)
        self.__repo - a

    def search_by_date_and_time(self, item_date, item_time):
        """Returns a list of activities that match the given date and time

        Arguments:
            item_date - date
            item_time - time

        Returns:
            list - the list of activities matching the date and time
        """
        l = self.get_all()
        list = []
        for i in l:
            if str(item_date) == str(i.date) and str(item_time) == str(i.time):
                list.append(i)
        return list

    def __search_by_date(self, item_date):
        """Returns a list of activities that match the given date and time

        Arguments:
            item_date - date
            item_time - time

        Returns:
            list - the list of activities matching the date and time
        """
        l = self.get_all()
        list = []
        for i in l:
            if str(item_date) == str(i.date):
                list.append(i)
        return list

    def search_by_description(self, item):
        """Returns a list of activities that match the given description

        Arguments:
            item - the description

        Returns:
            list- the list of all activities matching the description
        """
        l = self.get_all()
        list = []
        for i in l:
            if item.lower() in i.description.lower():
                list.append(i)
        return list

    def stats_activities_day(self, day):
        """
        Return the sorted list of all activities

        Arguments:
            day

        Returns:
            list - the list of sorted dates
        """
        list = sorted(self.__search_by_date(day), key=lambda k: k.time)
        return list

    def busiest_days(self):
        """Returns all days ordered by the number of activities

        Returns:
            out - a strig of days that should be printed
        """
        out = ""
        days = {}
        for i in self.get_all():
            if i.date not in days:
                days[i.date] = 1
            else:
                days[i.date] += 1

        sorted_x = sorted(days.items(), key=operator.itemgetter(1), reverse=True)
        for i in sorted_x:
            out = out + "Day " + str(i[0]) + " has " + str(i[1]) + " activities\n"
        return out

    def get_activities_for_person(self, person_id):
        """Return all activities in which a person is enroled

        Arguments:
            person_id - the entity_id of the person

        Returns:
            activities_of_person - the said list
        """
        activities = self.get_all()
        activities_of_person = []
        for i in activities:
            for j in i.person_ids:
                if j.person_id == person_id:
                    activities_of_person.append(i.entity_id)
        return activities_of_person

    def busiest_persons(self):
        """Return a list of all persons ordered by the number of activities they are enroled in

        Returns:
            out - a string that should be printed
        """
        activities = self.get_all()
        busy_persons = {}
        out = ""
        for i in activities:
            for j in i.person_ids:
                if j.person_id not in busy_persons:
                    busy_persons[j.person_id] = 1
                else:
                    busy_persons[j.person_id] += 1
        sorted_x = sorted(busy_persons.items(), key=operator.itemgetter(1), reverse=True)
        for i in sorted_x:
            out = out + "The person with entity_id " + str(i[0]) + " whill attend  " + str(i[1]) + " activities\n"
        return out

    def get_all(self):
        """Returns all the activities in the repository"""
        return self.__repo.get_all()
