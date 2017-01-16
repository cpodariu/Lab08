class Repository(object):
    def __init__(self):
        self._entities = {}

    def save(self, a):
        self._entities[a.entity_id] = a

    def delete(self, a):
        del self._entities[a.entity_id]

    def get_all(self):
        l = []
        for v in self._entities.values():
            l.append(v)
        return l

    def get_all_ids(self):
        """Returns a list of all IDs in the repository

        Returns:
             l - the list
        """
        l = []
        for v in self._entities.keys():
            l.append(v)
        return l

    def get_by_id(self, x):
        for i in self._entities.values():
            if i.entity_id == x:
                return i

    def __add__(self, other):
        self.save(other)

    def __radd__(self, other):
        self.save(other)

    def __sub__(self, other):
        self.delete(other)
