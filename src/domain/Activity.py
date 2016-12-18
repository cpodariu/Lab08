from domain.Appointment import Appointment
from domain.Person import Person


class Activity(object):
    """Stores an activity"""

    def __init__(self, entity_id, appointments, date, time, description):
        self.__entity_id = int(entity_id)
        self.__appointments = appointments
        self.__date = int(date)
        self.__time = int(time)
        self.__description = description

    @staticmethod
    def convert(line):
        lst = line.split(',')
        length = len(lst)
        id = lst[0]
        description = lst[length - 1].strip("\n")
        time = lst[length - 2]
        date = lst[length - 3]
        activities = []
        for i in lst[1:length-3]:
            a = Appointment(i, id)
            activities.append(a)
        activity_object = Activity(id, activities, date, time, description)
        return activity_object

    @staticmethod
    def parse(entity):
        appointments = ""
        for i in entity.person_ids:
            appointments += ","
            appointments += str(i.person_id)
        line = "{0}{1},{2},{3},{4}".format(entity.entity_id, appointments, str(entity.date), str(entity.time), entity.description)
        return line


    @property
    def entity_id(self):
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, value):
        self.__entity_id = int(value)

    @property
    def person_ids(self):
        return self.__appointments

    @person_ids.setter
    def person_ids(self, value):
        self.__appointments = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = int(value)

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = int(value)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __str__(self):
        appoint_str = ""
        for i in self.__appointments:
            appoint_str += str(i.person_id)
            appoint_str += ", "
        appoint_str = appoint_str[:-2]
        return "ID: " + str(self.__entity_id) + ', Participants: ' + appoint_str + ', Date: ' + str(self.__date) \
               + ', Time: ' + str(self.__time) + ', Description: ' + str(self.__description)