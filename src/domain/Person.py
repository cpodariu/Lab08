class Person(object):
    """Class for persons"""

    def __init__(self, entity_id, entity_name, phone_number, address):
        self.__entity_id = int(entity_id)
        self.__entity_name = entity_name
        self.__phone = phone_number
        self.__address = address

    @staticmethod
    def parse(entity):
        line = "{0},{1},{2},{3}".format(str(entity.entity_id), entity.entity_name, str(entity.phone_number), str(entity.address))
        return line

    @staticmethod
    def convert(line):
        lst = line.split(',')
        pers = Person(lst[0], lst[1], lst[2], lst[3].strip('\n'))
        return pers

    @property
    def entity_id(self):
        return self.__entity_id

    @entity_id.setter
    def entity_id(self, value):
        self.__entity_id = int(value)

    @property
    def entity_name(self):
        return self.__entity_name

    @entity_name.setter
    def entity_name(self, value):
        self.__entity_name = value

    @property
    def phone_number(self):
        return self.__phone

    @phone_number.setter
    def phone_number(self, value):
        self.__phone = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def __str__(self):
        return "ID: " + str(
            self.__entity_id) + ', Name: ' + self.__entity_name + ', Phone: ' + self.__phone + ', Address: ' + self.__address
