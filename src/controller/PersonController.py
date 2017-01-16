import random
import string
from copy import deepcopy

from src.domain.Person import Person
from src.validators.PersonValidator import PersonValidator


class PersonController:
    def __init__(self, repo):
        self.__repo = repo
        self.__validator = PersonValidator
        self.__undo = []
        self.__undoable_operations = 0

    def copy_repo(self):
        """Creates a copy of the repository and stores it"""
        if self.__undoable_operations == 0:
            self.__undo = [deepcopy(self.__repo)]
            self.__undoable_operations += 1
        else:
            self.__undo = self.__undo[:self.__undoable_operations]
            self.__undo.append(deepcopy(self.__repo))
            self.__undoable_operations += 1

    def undo_operation(self):
        """Move the previous made copy of the repository into the current repository"""
        if self.__undoable_operations != 0:
            if len(self.__undo) == self.__undoable_operations:
                self.__undoable_operations -= 2
            else:
                self.__undoable_operations -= 1
            self.__repo = self.__undo[self.__undoable_operations]

    def redo_operation(self):
        """Redo an operation, where possible"""
        if self.__undoable_operations < len(self.__undo):
            self.__undoable_operations += 1
            self.__repo = self.__undo[self.__undoable_operations]

    def add_person(self, id, name, phone, address):
        """Creates a Person Object and adds it to the repository

        Arguments:
            entity_id - int
            name - str
            phone - str
            address - str
        """
        p = Person(id, name, phone, address)
        self.__validator.validate(p)
        self.__repo + p

    def remove_person(self, id, name, phone, address):
        """Removes a person from the repository

        Arguments:
            entity_id - int
            name - str
            phone - str
            address - str
        """
        p = Person(id, name, phone, address)
        self.__repo - p

    def get_all(self):
        """Returns all persons in the repository"""
        return self.__repo.get_all()

    def get_all_ids(self):
        """Returns all person IDs in the repository"""
        return self.__repo.get_all_ids()

    def search_by_name(self, item):
        """Returns a list of all Persons that match the given name

        Arguments:
            item - The name

        Returns:
            list - the list of person
        """
        l = self.get_all()
        lst = []
        for i in l:
            if item.lower() in i.entity_name.lower():
                lst.append(i)
        return lst

    def search_by_phone(self, item):
        """Returns a list of all persons that match the given phone number

        Arguments:
            item - The phone number

        Returns:
            list - the list of persons
        """
        l = self.get_all()
        list = []
        for i in l:
            if item.lower() in i.phone_number.lower():
                list.append(i)
        return list

    @staticmethod
    def __random_word(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    @staticmethod
    def __random_digits(length):
        return ''.join(random.choice(string.digits) for i in range(length))

    def populate_repo(self):
        for i in range(1, 100):
            self.add_person(i, self.__random_word(10), self.__random_digits(10), self.__random_word(6))