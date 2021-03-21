from django.db import models

# Create your models here.

class Empregado(models.Model):
    nome_completo= models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    telefone = models.CharField(max_length=15)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
