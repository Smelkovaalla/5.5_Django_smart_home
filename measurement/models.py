from django.db import models


class Temp_sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    date_create = models.DateTimeField(auto_now_add=True)


class Temp_measure(models.Model):
    temperature = models.FloatField()
    date_current = models.DateTimeField(auto_now=True)
    temp_sensor_id = models.ForeignKey(Temp_sensor, on_delete=models.CASCADE, related_name='sensor')