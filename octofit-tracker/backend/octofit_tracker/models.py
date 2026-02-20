from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    is_superhero = models.BooleanField(default=False)

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.CharField(max_length=48)  # Store ObjectId as string
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.CharField(max_length=48)  # Store ObjectId as string
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
