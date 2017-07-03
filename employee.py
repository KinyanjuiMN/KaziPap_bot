class Employee(object):
    """ class Employee
              attributes:
              name
              phone
              email
              speciality

    """
    def __init__(self, name, phone, email, speciality):
        self.name = name;
        self.phone =phone;
        self.email = email;
        self.speciality = speciality;
        self.employee =(\
                         self.name,\
                         self.phone,\
                         self.email,\
                         self.speciality \
                        )
    def get_employee(self):
        return self.employee;
    def get_employee_name(self):
        return self.name;
    def get_employee_phone(self):
        return self.phone;
    def get_employee_email(self):
        return self.email;
    def get_employee_speciality(self):
        return self.speciality;
    def __str__(self):
        return str(self.employee)
