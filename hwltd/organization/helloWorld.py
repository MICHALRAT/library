from hwltd.organization.employees import Employees
from workers.structure.worker import Worker
from workers.structure.engineer import Engineer
from workers.structure.salesPerson import SalesPerson
from workers.structure.group import Group
from hwltd.reports.reports import get_average_salary
from hwltd.reports.reports import get_num_employees
import sys
sys.setrecursionlimit(10000)


class HelloWorld:
    # organizational structure
    organizational_structure = [Group("Hello World", " ", None, None, [])]
    layer1 = [Group("Engineering Department", " ", organizational_structure, None, []),
              Group("HR Department", " ", organizational_structure, None, []),
              Group("Finance Department", " ", organizational_structure, None, [])]
    organizational_structure[0].subgroups = layer1  #
    layer2_fd = [Group("Salaries Group", " ", layer1[2], None, []),
                 Group("Budget Group", " ", layer1[2], None, [])]
    layer1[2].subgroups = layer2_fd  #
    layer2_hd = [Group("Recruitment Group", " ", layer1[1], []),
                 Group("Culture Group", " ", layer1[1], None, [])]
    layer1[1].subgroups = layer2_hd  #
    layer2_ed = [Group("SW Group", " ",  layer1[0], None, []),
                 Group("HW Group", " ",  layer1[0], None, []),
                 Group("CTO Group", " ", layer1[0], None, []),
                 Group("System Group", " ",  layer1[0], None, [])]
    layer1[0].subgroups = layer2_ed   #
    layer3_bg = [Group("Income Team", " ", layer2_fd[1], None, []),
                 Group("Outcome Team", " ", layer2_fd[1], None, [])]
    layer2_fd[1].subgroups = layer3_bg  #
    layer3_rg = [Group("Tech Team", " ", layer2_hd[0], None, []),
                 Group("Staff Team", " ",  layer2_hd[0], None, [])]
    layer2_hd[0].subgroups = layer3_rg  #
    layer3_syg = [Group("Design Team", " ", layer2_ed[2], None, []),
                  Group("Poc Team", " ", layer2_ed[2], None, [])]
    layer2_ed[2].subgroups = layer3_syg  #
    layer3_hwg = [Group("Chip Team", " ", layer2_ed[1], None, []),
                  Group("Board Team", " ", layer2_ed[1], None, []),
                  Group("Power Team", " ", layer2_ed[1], None, [])]
    layer2_ed[1].subgroups = layer3_hwg  #
    layer3_swg = [Group("Infrastructure Team", " ", layer2_ed[0], None, []),
                  Group("App Team", " ", layer2_ed[0], None, []),
                  Group("Drivers Team", " ", layer2_ed[0], None, []),
                  Group("QA Team", " ", layer2_ed[0], None, [])]
    layer2_ed[0].subgroups = layer3_swg

    employees = Employees()

    def __init__(self, file_path):
        self.company = []
        self.unpacking_structure(self.organizational_structure)
        self.file_path = file_path
        self.read_file()

    def read_file(self):
        with open(self.file_path) as file:  # Use file to refer to the file object
            data = file.read()
            self.fill_employees(data)

    def fill_employees(self, text):
        split_text = text.splitlines()
        for line in (line for line in split_text if not line.startswith('#') and not line == ""):
            x = line.split(", ")
            try:
                team_worker = self.parse_worker(x)
                self.insert_worker(self.organizational_structure, team_worker[0], team_worker[1])
                email = self.find_email(x)
                name = self.find_name(x)
                self.employees.add_employee(name, email)
            except ValueError as e:
                print(e)

    def insert_worker(self, struct, team, worker):
        for x in struct:
            if team == x.name.split(' ', 1)[0].lower():
                x.workers.append(worker)
            if x.subgroups is not None:
                self.insert_worker(x.subgroups, team, worker)

    @staticmethod
    def find_email(x):
        return x[3]

    @staticmethod
    def find_name(x):
        if not x[0] or not x[1]:
            raise ValueError("first and last name must be filled in")
        return x[0] + " " + x[1]

    def unpacking_structure(self, group):
            for x in group:
                # print(x.name)
                self.company.append(x.name.split(' ', 1)[0].lower())
                if x.subgroups is not None:
                    self.unpacking_structure(x.subgroups)

    def parse_worker(self, line):
        phone = line[4].split(";")
        address = line[5]
        team = self.check_team(line[6])
        role_salary = self.check_role(line[7], line[8])
        if role_salary == "worker":
            worker = Worker(line[1], line[0], line[2], line[3], address, phone, line[8])
        elif role_salary == "engineer":
            lis = line[8].split(";")
            worker = Engineer(line[1], line[0], line[2], line[3], address, phone, lis[0], lis[1])
        else:
            sal = line[8].split(";")
            deal = sal
            deal.pop(0), deal.pop(1)
            worker = SalesPerson(line[1], line[0], line[2], line[3], address, phone, sal[0], sal[1], deal)
        return team, worker

    def check_team(self, team):
        if team.lower() not in self.company:
            raise ValueError("team value incorrect, this team does nt exist")
        return team

    @staticmethod
    def check_role(role, salary):
        roles = (("staff", 1), ("engineer", 2), ("sales", 2))
        if role == roles[0][0] and len(salary.split(";")) == roles[0][1]:
            return "worker"
        if role == roles[1][0] and len(salary.split(";")) == roles[1][1]:
            return "engineer"
        elif role == roles[2][0] and len(salary.split(";")) >= roles[2][1]:
            return "sales person"
        else:
            raise ValueError("incorrect value for role: " + role + " and data: " + salary)


hw = HelloWorld("prework-task2-data.txt")
print(get_average_salary(hw.layer3_swg[3]))
# hw.unpacking_structure(hw.organizational_structure)
print(get_num_employees(hw.organizational_structure, 3))
