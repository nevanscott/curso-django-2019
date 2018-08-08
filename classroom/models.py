from django.db import models
from datetime import timedelta, date
from curriculum.models import Curriculum

class School(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Instance(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.curriculum) + ' ' + str(self.location) + ' ' + str(self.start_date)
    def class_days(self):
        dates = []
        for n in range(int((self.end_date + timedelta(1) - self.start_date).days)):
            date = self.start_date + timedelta(n)
            if date.weekday() not in (5,6):
                dates.append(date)
        return dates
    def schedule(self):
        dates = self.class_days()
        schedule = []
        for date in dates:
            schedule.append({
                    'date': date,
                    'events': Event.objects.filter(instance=self).filter(date=date)
                })
        return schedule

class Event(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
