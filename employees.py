from employee import Employee
class Employees(object):
    """ class Employees keeps a list of employees in a dictionary """
    def __init__(self):
        self.listOfEmployees = dict();

    def add_employee(self,name,phone,email,speicality):
        worker = Employee(name,phone,email,speciality);
        if name not in self.listOfEmployees:
           self.listOfEmployees.update({name:worker});

    def get_employee(self,name):
        return self.listOfEmployees[name].get_employee();

    def show_employees(self):
        for emp in self.listOfEmployees:
            print(self.listOfEmployees[emp] + "\n");

    def remove_employee(self,name):
        if name in self.listOfEmployees:
           del self.listOfEmployees[name]

    def employee_exists(self,name):
        if name in self.listOfEmployees:
            return True;
        else:
            return False;
