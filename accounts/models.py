from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    facilities = models.TextField()
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'{self.room.name} Booking from {self.start} to {self.end}'
