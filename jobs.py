from job import Job

class Jobs(object):
    """ class Jobs keeps a list of available jobs in a dictionary """

    def __init__(self):
        self.available_jobs = dict();

    def add_job(self,job_id,description,location,duration,payment,employer,chat_id):
       work = Job(job_id,description,location,duration,payment,employer,chat_id);
       if not self.job_exists(job_id):
          self.available_jobs.update({job_id:work});

    def remove_job(self,job_id):
        if self.job_exists(job_id):
           del self.available_jobs[job_id];

    def get_job(self,job_id):
        return self.available_jobs[job_id].get_job();

    def show_jobs(self):
        for item in self.available_jobs:
            print (self.available_jobs[item]);

    def job_exists(self,job_id):
        if job_id in self.available_jobs:
            return True;
        else:
            return False;
