class Appointment(object):
    """Class for appointments"""
    unique_id = 0

    def __init__(self, person_id, activity_id):
        self.__entity_id = Appointment.unique_id
        self.__person_id = person_id
        self.__activity_id = activity_id
        Appointment.unique_id += 1

    @property
    def entity_id(self):
        return self.__entity_id

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, value):
        self.__person_id = value

    @property
    def activity_id(self):
        return self.__activity_id

    @activity_id.setter
    def activity_id(self, value):
        self.__activity_id = value

    @staticmethod
    def convert(line):
        lst = line.split(',')
        app = Appointment(lst[1], lst[2].strip('\n'))
        return app

    @staticmethod
    def parse(entity):
        line = "{0},{1},{2}".format(entity.entity_id, entity.person_id, entity.activity_id)
        return line

    def __str__(self):
        return str(self.__person_id)
