from django.db import models

class Reading(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    def __str__(self):
        return self.title
    def curricula(self):
        return Curriculum.objects.filter(version__unit__lesson__readings__in=[self])

class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def readings(self):
        return Reading.objects.filter(lesson__unit__version__curriculum=self)
    def lessons(self):
        return Lesson.objects.filter(unit__version__curriculum=self)

class Version(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    number = models.CharField(max_length=16)
    def __str__(self):
        return self.number

class Unit(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    def __str__(self):
        return self.name

class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    readings = models.ManyToManyField(Reading)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    order = models.IntegerField()
    def __str__(self):
        return self.name

class Week(models.Model):
    number = models.IntegerField()
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

class Day(models.Model):
    number = models.IntegerField()
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)
