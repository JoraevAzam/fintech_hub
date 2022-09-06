from django.db import models
from uuid import uuid4


RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'courses/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


class CourseModel(models.Model):
    image = models.ImageField(upload_to=upload_location)
    teacher_image = models.ImageField(upload_to=upload_location)
    teacher = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)
    price = models.CharField(max_length=255)
    lessons_amount = models.CharField(max_length=255)
    teacher_level = models.CharField(max_length=255)
    lesson_duration = models.CharField(max_length=255)

    def __str__(self):
        return str(f"{self.id}-{self.course}-{self.teacher}")
