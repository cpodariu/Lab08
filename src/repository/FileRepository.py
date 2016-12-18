from src.repository.Repository import Repository


class FileRepository(Repository):
    def __init__(self, entity_class, file):
        super().__init__()
        self.__entity_class = entity_class
        self.__file = file
        self.read_file()

    def read_file(self):
        with open(self.__file) as f:
            for line in f:
                entity = self.__entity_class.convert(line)
                self._entities[entity.entity_id] = entity

    def write_file(self):
        with open(self.__file, "w") as f:
            lst = super().get_all()
            for i in lst:
                line = self.__entity_class.parse(i)
                f.write(line + '\n')

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
