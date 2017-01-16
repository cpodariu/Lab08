class AppointmentValidatorException(Exception):
    pass


def appointment_ids_validate(person_ids, persons):
    """Checks if the ids are valid ids of persons

    Arguments:
        person_ids - a list of ids
        persons - list of ids of persons that are already memorised

    Raises:
        ActivityValidatorException
    """
    for x in person_ids:
        if x not in persons:
            raise AppointmentValidatorException("Person IDs could not be found")