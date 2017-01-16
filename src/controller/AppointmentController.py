from domain.Appointment import Appointment
from validators.AppointmentValidator import appointment_ids_validate


class AppointmentController:
    def __init__(self, repo, person_repo):
        self.__repo = repo
        self.__person_repo = person_repo

    def make_appointments(self, person_ids, activity_id):
        """Makes new appointments and stores them in the appointment repository

        Arguments:
            person_ids - the list of person ids
            activity_id - the entity_id of the activity

        Returns:
            appointments - a list of Appointment objects
        """
        appointment_ids_validate(person_ids, self.__person_repo.get_all_ids())
        appointments = []
        for i in person_ids:
            a = Appointment(i, activity_id)
            appointments.append(a)
            self.__repo + a
        return appointments

    def remove_by_person_id(self, p_id):
        """Removes all appointments that contain the person entity_id

        Arguments:
            p_id - person entity_id
        """
        self.__repo.remove_appointment_by_person_id(p_id)

    def remove_by_activity_id(self, a_id):
        """Removes all appointments that contain the activity entity_id

        Arguments:
            a_id - activity_id
        """
        self.__repo.remove_appointment_by_activity_id(a_id)