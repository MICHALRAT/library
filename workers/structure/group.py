"""Class that defines a group in the organization"""
from workers.structure.worker import Worker


class Group:

    def __init__(self, name, description=None, parent_group=None, subgroups=[], workers=[]):
        self.name = name
        self.description = description
        self.parent_group = parent_group
        self.subgroups = subgroups
        self.workers = workers

    def add_subgroup(self, name, description, parent_group, work=[]):
        g = Group(name, description, parent_group)
        for x in work:
            g.workers.append(x)
        self.subgroups.append(g)

    def add_worker(self, first_name, last_name, year_of_birth, email, address, phones, salary):
        self.workers.append(Worker(first_name, last_name, year_of_birth, email, address, phones, salary))

    def get_workers(self):  # needs to be checked
        if not self.subgroups:
            return self.workers
        return self.get_sub_workers(self.subgroups)

        flatten_matrix = [val for self.subgroups.workers in self.subgroups for val in self.subgroups.workers]
        return self.workers+flatten_matrix

    def get_sub_workers(self, subgroups):
        for x in subgroups:
            print(x.name)
            if x.workers is not None:
                return self.get_workers(x.subgroups)

    def get_parents(self):
        ls = []
        pg = self.parent_group
        while pg is not None:
            ls.append(self.parent_group)
            ls.append(self.parent_group.get_parents())
            pg.pop(0)  # removing the parent from the temp list so that the loop will stop when done
        return ls
