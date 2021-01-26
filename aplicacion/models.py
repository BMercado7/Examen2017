from django.db import models

# Create your models here.
class paciente(models.Model):
    nombreP = models.CharField(max_length = 128)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class medico(models.Model):
    nombreM = models.CharField(max_length = 128)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class receta(models.Model):
    idMedico = models.ForeignKey(medico, null=True, on_delete=models.CASCADE)
    idPaciente = models.ForeignKey(paciente, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
