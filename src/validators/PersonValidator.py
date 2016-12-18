class PersonException(Exception):
    pass


class PersonValidatorException(PersonException):
    pass


class PersonValidator(object):
    @staticmethod
    def validate(person):
        """Function that raises flags if the person is not valid

        Arguments:
             person - a Person object

        Raises:
            PersonValidatorException
        """
        if not type(person.entity_id) is int:
            raise PersonValidatorException("ID must be an int")

        if not person.entity_id > 0:
            raise PersonValidatorException("ID must be greater than 0")

        if not type(person.entity_name) is str:
            raise PersonValidatorException("Name must be a string")

        if not type(person.phone_number) is str:
            raise PersonValidatorException("Phone number must be a string")

        for i in person.phone_number:
            if i < "0" or i > "9":
                raise PersonValidatorException("Person Phone Number must be made only of numbers")
