import pickle

from repository.Repository import Repository


class BinaryRepository(Repository):
    def __init__(self, entity_class: object, file: object) -> object:
        super().__init__()
        self.__entity_class = entity_class
        self.__file = file
        self.read_file()

    def read_file(self):
        try:
            with open(self.__file, "rb") as f:
                entity = pickle.load(f)
                for i in entity:
                    super().save(i)
        except EOFError:
            pass

    def write_file(self):
        with open(self.__file, "wb") as f:
            lst = super().get_all()
            pickle.dump(lst, f)

    def save(self, entity):
        super().save(entity)
        self.write_file()

    def delete(self, entity_id):
        super().delete(entity_id)
        self.write_file()

    def get_by_id(self, entity_id):
        return super().get_by_id(entity_id)

    def get_all(self):
        return super().get_all()

    def __add__(self, other):
        self.save(other)

    def __radd__(self, other):
        self.save(other)

    def __sub__(self, other):
        self.delete(other)
