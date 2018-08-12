from django.core.management.base import BaseCommand, CommandError
from curriculum.models import Reading, Lesson, Curriculum, Version, Unit, Week, Day
import urllib.request, json

# FIXME: This depends on having hiccup running locally
source = "http://localhost:3000/"


class Command(BaseCommand):
    help = 'Imports curriculum materials'

    def handle(self, *args, **options):
        with urllib.request.urlopen(source) as url:
            data = json.loads(url.read().decode())
            self.stdout.write(data['description'])
            self.stdout.write(data['version'])
            curriculum, created = Curriculum.objects.get_or_create(name=data['description'])
            version, created = Version.objects.get_or_create(number=data['version'], curriculum=curriculum)
            order = 0
            for lesson in data['lessons']:
                self.stdout.write('========================')
                self.stdout.write(lesson['slug'])
                unit, created = Unit.objects.get_or_create(
                    name="Unit "+str(lesson['unit']),
                    version=version,
                    defaults={
                        'order': lesson['unit']
                    }
                )
                if 'week' in lesson:
                    week, created = Week.objects.get_or_create(
                        number=(lesson['unit']*3 - 3) + lesson['week'],
                        version=version
                    )
                    if 'day' in lesson:
                        day, created = Day.objects.get_or_create(
                            number=lesson['day'],
                            week=week
                        )
                reading, created = Reading.objects.get_or_create(
                    slug=lesson['slug'],
                    defaults={
                        'title': lesson['title'],
                        'body': lesson['contents']
                    }
                )
                reading.body = lesson['contents']
                reading.save()
                myLesson, created = Lesson.objects.get_or_create(
                    slug=lesson['slug'],
                    defaults={
                        'name': lesson['title'],
                        'unit': unit,
                        'order': order
                    }
                )
                myLesson.name = lesson['title']
                myLesson.order = order
                myLesson.readings.add(reading)
                if 'day' in locals():
                    day.lessons.add(myLesson)
                    day.save()
                self.stdout.write(reading.title)
                myLesson.save()
                order += 1
                self.stdout.write('--------------------------')
