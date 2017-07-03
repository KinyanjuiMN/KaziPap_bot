
from employer import Employer

class Employers(object):
    """ class Employers keeps a list of employers in a dictionary """

    def __init__(self):
        self.listOfEmployers =dict();

    def add_employer(self,name,phone,email,contact):
        emp = Employer(name,phone,email,contact)
        if not self.employer_exists(name):
            self.listOfEmployers.update({emp.name:emp});

    def remove_employer(self,key):
        if self.employer_exists(key):
            del self.listOfEmployers[emp.name];

    def show_employers(self):
         for emp in self.listOfEmployers:
             print(self.listOfEmployers[emp].get_employer());

    def get_employers(self):
        return self.listOfEmployers;

    def get_employer(self,name):
        return self.listOfEmployers[name].get_employer();

    def employer_exists(self,key):
        if key in self.listOfEmployers:
            return True;
        else:
            return False;

    def __str__(self):
        return str(self.listOfEmployers);
