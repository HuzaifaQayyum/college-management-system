from django.db import models

class CourseManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class SubjectManager(models.Manager):
    
    def get_by_natural_key(self, name):
        return self.get(name=name)


