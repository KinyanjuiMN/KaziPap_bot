class Employer(object):
    """ class Employer 
        attributes:
             name
             phone
             email
             contact
    """
    def __init__(self,name,phone,email,contact):
        self.name = name;
        self.phone = phone;
        self.email = email;
        self.contact =contact;
        self.employer =(\
                         self.name,\
                         self.phone,\
                         self.email,\
                         self.contact\
                         )
    def set_employer(self,name,phone,email,contact):
        self.name = name;
        self.phone = phone;
        self.email = email;
        self.contact = contact;
        self.employer =(\
                         self.name,\
                         self.phone,\
                         self.email,\
                         self.contact,\
                         )
    def get_employer(self):
       return self.employer;

    def get_employer_name(self):
        return self.name;

    def get_employer_phone(self):
        return self.phone;

    def get_employer_email(self):
        return self.email;

    def get_employer_contact(self):
        return self.contact;
    def __str__(self):
      return str(self.employer) ;
