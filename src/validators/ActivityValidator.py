class ActivityValidatorException(Exception):
    pass

class ActivityValidator(object):
    @staticmethod
    def validate(activity):
        """Validates an activity

        Arguments:
            activity - an Activity type object

        Raises:
            ActivityValidatorException
        """
        if not type(activity.entity_id) is int:
            raise ActivityValidatorException("Activity ID must be an int")
        try:
            date = int(activity.date)
            time = int(activity.time)
        except:
            raise ActivityValidatorException("Date and time must be integers")
        if date < 1 or date > 32:
            raise ActivityValidatorException("The date is not valid")
        if time < 0 or time > 24:
            raise ActivityValidatorException("The time is not valid")

    @staticmethod
    def activity_ids_validate(appointments, persons):
        """Chacks if the ids are valid ids of persons

        Arguments:
            person_ids - a list of ids
            persons - list of ids of persons that are already memorised

        Raises:
            ActivityValidatorException
        """
        for x in appointments:
            if x.person_id not in persons:
                raise ActivityValidatorException("Person IDs could not be found")

    @staticmethod
    def activity_date_validate(date, time, activity_list):
        for x in activity_list:
            if x.date == int(date) and x.time == int(time):
                raise ActivityValidatorException("Date and time already exist")