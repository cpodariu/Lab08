from controller.ActivityController import ActivityController
from controller.AppointmentController import AppointmentController
from controller.PersonController import PersonController
from domain.Activity import Activity
from domain.Appointment import Appointment
from domain.Person import Person
from domain.Settings import Settings
from repository.BinaryRepository import BinaryRepository
from repository.FileRepository import FileRepository
from repository.Repository import Repository
from ui.console import Console

if __name__ == '__main__':
    settings = Settings()
    if settings.repo_mode == "inmemory":
        person_repository = Repository()
        activity_repository = Repository()
        appointment_repository = Repository()
    elif settings.repo_mode == "textfile":
        person_repository = FileRepository(Person, settings.persons_repo)
        activity_repository = FileRepository(Activity, settings.activity_repo)
        appointment_repository = FileRepository(Appointment, settings.apppoinment_repo)
    elif settings.repo_mode == "binary":
        person_repository = BinaryRepository(Person, settings.persons_repo)
        activity_repository = BinaryRepository(Activity, settings.activity_repo)
        appointment_repository = BinaryRepository(Appointment, settings.apppoinment_repo)


    personCtrl = PersonController(person_repository)
    activityCtrl = ActivityController(activity_repository, person_repository)
    appointmentCtrl = AppointmentController(appointment_repository, person_repository)
    print("Controllers created")

    cons = Console(personCtrl, activityCtrl, appointmentCtrl)
    print("Console created")

    # personCtrl.populate_repo()
    # print("Person Repository populated")
    # cons.populate_activity()
    # print("Repositories populated")

    cons.run()
