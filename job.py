class Job(object):
    """ class Job attributes:
                 job_id
                 description
                 employer
                 location
                 duration
                 Payment
                 chat_id

    """
    def __init__(self,job_id,description,location,duration,payment,employer,chat_id):
      self.job_id = job_id;
      self.description = description;
      self.location = location;
      self.duration = duration;
      self.payment = payment;
      self.employer = employer;
      self.chat_id = chat_id;
      self.job = (\
                  self.job_id,\
                  self.description,\
                  self.location,\
                  self.duration,\
                  self.payment,\
                  self.employer,\
                  self.chat_id\
                  );

    def get_job(self):
        return self.job;

    def get_job_id(self):
        return self.job_id;

    def get_job_description(self):
        return self.description;

    def get_job_location(self):
        return self.location;

    def get_job_duration(self):
        return self.duration;

    def get_job_payment(self):
        return self.payment;

    def get_job_employer(self):
        return self.employer;

    def get_job_chat_id(self):
        return self.chat_id;

    def __str__(self):
        return str(self.job);
