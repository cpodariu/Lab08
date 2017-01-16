import random
import string

from validators.ActivityValidator import ActivityValidator
from validators.PersonValidator import PersonValidatorException


class Console:
    def __init__(self, person_ctrl, activity_ctrl, appointment_ctrl):
        self.__person_ctrl = person_ctrl
        self.__activity_ctrl = activity_ctrl
        self.__appointment_ctrl = appointment_ctrl
        self.__activity_validator = ActivityValidator()
        self.__undoable_operations = []

        self.__commandsList = {"1": self.__ui_add_person, "2": self.__ui_update_person,
                               "3": self.__ui_id_remove, "4": self.__show_all_persons,
                               "5": self.__uiAddActivity, "6": self.__uiUpdateActivity,
                               "7": self.__uiRemoveActivity, "8": self.__showAllActivity,
                               "9": self.__uiSearch, "0": self.__ui_statistics_menu,
                               "10": self.__undo, "11": self.__redo}
        self.__commandListMessage = "Command options:\n" \
                                    "1 - Add a new person\n" \
                                    "2 - Update person\n" \
                                    "3 - Remove a person\n" \
                                    "4 - Show all persons\n" \
                                    "5 - Add a new activity\n" \
                                    "6 - Update activity\n" \
                                    "7 - Remove activity\n" \
                                    "8 - Show All Activities\n" \
                                    "9 - Search Menu\n" \
                                    "0 - Statistics\n" \
                                    "10 - Undo\n" \
                                    "11 - Redo\n" \
                                    "exit - To exit the program"

    def __print_list_of_objects(self, list):
        st = ""
        for x in list:
            st += str(x) + "\n"
        st = st[:-1]
        print(st)

    def __readIds(self):
        """Reads a list of IDs and returns it

        Returns:
            nums - list of ids
        """
        try:
            a = input()
        except:
            print('Invalid input')
            return self.__readIds()
        nums = [int(n) for n in a.split()]
        return nums

    def __read_command(self):
        """Reads a command and returns it"""
        try:
            return input()
        except:
            print("You have to give a command")
            return self.__read_command()

    def __read_input(self, message):
        """Reads the input and returns it"""
        try:
            print(message)
            a = input()
            return a
        except:
            raise TypeError("Invalid Input!")



            # *************START***PERSONS RELATED FUNCTIONS*************

    def __ui_add_person(self):
        try:
            id = int(self.__read_input("Person ID:"))
        except:
            raise TypeError("The entity_id must be an integer!")
        name = self.__read_input("Name:")
        phone = self.__read_input("Phone number:")
        address = self.__read_input("Address:")
        self.__person_ctrl.add_person(id, name, phone, address)
        self.__copy_repository()

    def __ui_update_person(self):
        try:
            id = int(self.__read_input("The entity_id of the person you want to update:"))
        except:
            raise TypeError("Invalid inputs")
        name = self.__read_input("The name of the person you want to update:")
        phone = self.__read_input("The phone number of the person you want to update:")
        address = self.__read_input("The address of the person you want to update:")
        self.__person_ctrl.remove_person(id, 'a', 'a', 'a')
        self.__appointment_ctrl.remove_by_person_id(id)
        self.__person_ctrl.add_person(id, name, phone, address)
        self.__copy_repository()

    def __ui_id_remove(self):
        try:
            person_ID = int(self.__read_input("The ID of the person you want to remove:"))
        except:
            raise TypeError("The Id must be an integer")
        self.__person_ctrl.remove_person(person_ID, "a", "a", "a")
        self.__appointment_ctrl.remove_by_person_id(person_ID)
        self.__copy_repository()

    def __show_all_persons(self):
        self.__print_list_of_objects(self.__person_ctrl.get_all())

    # *************END***PERSONS RELATED FUNCTIONS*************

    # *************START***ACTIVITY RELATED FUNCTIONS*************

    def populate_activity(self):
        for i in range(1, 100):
            no_of_ids = random.randint(1, 20)
            person_ids = []
            for j in range(0, no_of_ids):
                random_int = random.randint(1, 99)
                while random_int in person_ids:
                    random_int = random.randint(1, 99)
                person_ids.append(random_int)
            date = str(random.randint(1, 30))
            time = str(random.randint(1, 24))
            is_valid = True
            try:
                self.__activity_validator.activity_date_validate(date, time, self.__activity_ctrl.get_all())
            except:
                is_valid = False

            while not is_valid:
                date = str(random.randint(1, 30))
                time = str(random.randint(1, 24))
                try:
                    self.__activity_validator.activity_date_validate(date, time, self.__activity_ctrl.get_all())
                    is_valid = True
                except:
                    is_valid = False
            description = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
            appointments = self.__appointment_ctrl.make_appointments(person_ids, i)
            self.__activity_ctrl.save(i, appointments, date, time, description)


    def __uiAddActivity(self):
        try:
            id = int(self.__read_input("Activity entity_id:"))
        except:
            raise TypeError("The ID must be an integer!")
        print("Person ids(Separated by ' '):")
        person_ids = self.__readIds()
        date = self.__read_input("Date:")
        time = self.__read_input("Time:")
        description = self.__read_input("Description:")
        appointments = self.__appointment_ctrl.make_appointments(person_ids, id)
        self.__activity_ctrl.save(id, appointments, date, time, description)
        self.__copy_repository()

    def __showAllActivity(self):
        st = ""
        for x in self.__activity_ctrl.get_all():
            st += str(x) + "\n"
        st = st[:-1]
        print(st)

    def __uiUpdateActivity(self):
        try:
            id = int(self.__read_input("Activity entity_id:"))
        except:
            raise TypeError("The ID must be an integer!")
        print("Person ids(Separated by ' '):")
        person_ids = self.__readIds()
        date = self.__read_input("Date:")
        time = self.__read_input("Time:")
        description = self.__read_input("Description:")
        appointments = self.__appointment_ctrl.make_appointments(person_ids, id)
        self.__activity_ctrl.delete(id, [], 0, 0, ' ')
        self.__appointment_ctrl.remove_by_activity_id(id)
        self.__activity_ctrl.save(id, appointments, date, time, description)
        self.__copy_repository()

    def __uiRemoveActivity(self):
        try:
            activity_id = int(self.__read_input("The ID of the activity you want removed:"))
        except:
            print("The ID must be an integer!")
            self.__uiRemoveActivity()
            return
        self.__activity_ctrl.delete(activity_id, [], 0, 0, ' ')
        self.__appointment_ctrl.remove_by_activity_id(activity_id)
        self.__copy_repository()

    # *************END***ACTIVITY RELATED FUNCTIONS*************

    # *************START***SEARCH RELATED FUNCTIONS*************
    def __uiSearch(self):
        menu = "1 - Search for persons\n" \
               "2 - search for activities\n"
        person_menu = "1 - Search by name\n" \
                      "2 - Search by phone number\n"
        activity_menu = "1 - Search by date/time\n" \
                        "2 - Search by descriprion"
        print(menu)
        command = self.__read_command()
        if command == '1':
            print(person_menu)
            command = self.__read_command()
            term = self.__read_input("Search item:")
            if command == '1':
                self.__print_list_of_objects(self.__person_ctrl.search_by_name(term))
            if command == '2':
                self.__print_list_of_objects(self.__person_ctrl.search_by_phone(term))
        if command == '2':
            print(activity_menu)
            command = self.__read_command()
            if command == '1':
                date = self.__read_input("Date:")
                time = self.__read_input("Time:")
                self.__print_list_of_objects(self.__activity_ctrl.search_by_date_and_time(date, time))
            if command == '2':
                item = self.__read_input("Search item:")
                self.__print_list_of_objects(self.__activity_ctrl.search_by_description(item))

    # *************END***SEARCH RELATED FUNCTIONS*************

    # *************START***STATISTICS RELATED FUNCTIONS*************

    def __ui_activities_day(self):
        # day = self.__read_input("Day:")
        # self.__activity_ctrl.stats_activities_day(day)
        self.__print_list_of_objects(self.__activity_ctrl.stats_activities_day(self.__read_input("Day:")))

    def __ui_busiest_days(self):
        print(self.__activity_ctrl.busiest_days())

    def __ui_activities_with_person(self):
        person = int(self.__read_input("Person entity_id:"))
        list = self.__activity_ctrl.get_activities_for_person(person)
        print("The person with entity_id " + str(person) + " will participate in the following activities:\n")
        print(list)

    def __ui_busiest_person(self):
        print(self.__activity_ctrl.busiest_persons())

    def __ui_statistics_menu(self):
        statistics_commands = "1 - Activities for a given day/week\n" \
                              "2 - Busiest days\n" \
                              "3 - Activities of a person\n" \
                              "4 - Busiest person"
        statistics_functions = {"1": self.__ui_activities_day, "2": self.__ui_busiest_days,
                                "3": self.__ui_activities_with_person, "4": self.__ui_busiest_person}
        print(statistics_commands)
        command = self.__read_command()
        while command not in statistics_functions:
            print("Invalid command")
            command = self.__read_command()
        statistics_functions[command]()

    # *************END***STATISTICS RELATED FUNCTIONS*************

    def __undo(self):
        self.__person_ctrl.undo_operation()
        self.__activity_ctrl.undo_operation()

    def __redo(self):
        self.__person_ctrl.redo_operation()
        self.__activity_ctrl.redo_operation()

    def __copy_repository(self):
        self.__person_ctrl.copy_repo()
        self.__activity_ctrl.copy_repo()

    def run(self):
        self.__copy_repository()
        while True:
            print(self.__commandListMessage)
            cmd = self.__read_command()
            if cmd == 'exit':
                return
            if cmd in self.__commandsList:
                try:
                    self.__commandsList[cmd]()
                except PersonValidatorException as c:
                    print(c)
                except TypeError as c:
                    print(c)
                except AppointmentValidatorException as c:
                    print(c)
                except ActivityValidatorException as c:
                    print(c)
                except ValueError as c:
                    print(c)
                # except:
                #     print("undefined error")
            else:
                print("invalid command")
