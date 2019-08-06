from workers.structure.group import Group

def get_num_employees(department, depth):
    """"""
    dc = {}
    for x in department:
        # print(x.name)
        if x.subgroups is not None and depth != 0:
            return get_num_employees(x.subgroups, depth-1)
        else:
            dc = {x.name: len(x.workers)}
            print(dc)
    return dc


def get_relational_salary(group):
    """"""

def get_average_salary(group):
    """"""
    if group.workers is not None:
        sum = 0
        for x in group.workers:
            print("\n" + str(x.get_salary()))
            sum +=(x.get_salary())
        return sum/len(group.workers)
