from controller.ActivityController import ActivityController
from controller.AppointmentController import AppointmentController
from controller.PersonController import PersonController
from domain.Activity import Activity
from domain.Appointment import Appointment
from domain.Person import Person
from repository.BinaryRepository import BinaryRepository
from repository.FileRepository import FileRepository
from ui.console import Console



if __name__ == '__main__':
    # personRepo = FileRepository(Person ,"..\data\personRepo.txt")
    # activityRepo = FileRepository(Activity,"..\data\\activityRepo.txt")
    # appointmentRepo = FileRepository(Appointment,"..\data\\appointmentRepo.txt")
    personRepo = BinaryRepository(Person ,"..\data\personRepo.pickle")
    activityRepo = BinaryRepository(Activity,"..\data\\activityRepo.pickle")
    appointmentRepo = BinaryRepository(Appointment,"..\data\\appointmentRepo.pickle")
    print("Repositories created")

    personCtrl = PersonController(personRepo)
    activityCtrl = ActivityController(activityRepo, personRepo)
    appointmentCtrl = AppointmentController(appointmentRepo, personRepo)
    print("Controllers created")

    cons = Console(personCtrl, activityCtrl, appointmentCtrl)
    print("Console created")
    # personCtrl.populate_repo()
    # print("Person Repository populated")
    # cons.populate_activity()
    # print("Repositories populated")

    cons.run()
