from django.db import models

class GSLClientes(models.Model):
    nombre = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre