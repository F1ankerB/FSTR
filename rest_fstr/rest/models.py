from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class PerevalAdded(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coords, on_delete=models.CASCADE)
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.TextField()
    connect = models.TextField()
    add_time = models.DateTimeField()
    status = models.CharField(max_length=50, default='new')

class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    img = models.BinaryField()
    date_added = models.DateTimeField(auto_now_add=True)

class PerevalAreas(models.Model):
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE)
    title = models.TextField()

class SprActivitiesTypes(models.Model):
    title = models.TextField()

