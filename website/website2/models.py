from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length = 100)
    niveles_cursados = models.IntegerField()
    puntuacion_media = models.IntegerField()

    def __str__(self):
        return self.nombre