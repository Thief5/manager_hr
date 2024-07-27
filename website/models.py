from django.db import models
from django.contrib.auth.models import User

class Utilizatori(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='utilizator')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    DEPARTAMENT_CHOICES = [
        ('Gradinarit', 'Gradinarit'),
        ('Vopsele', 'Vopsele'),
        ('Tinichigerie', 'Tinichigerie'),
        ('Unelte', 'Unelte')
    ]

    NIVELURI_EXPERIENTA = [
        ('INCEPATOR', 'Începator'),
        ('INTERMEDIAR', 'Intermediar'),
        ('AVANSAT', 'Avansat'),
    ]
    
    departament = models.CharField(max_length=20, choices=DEPARTAMENT_CHOICES)
    nivel = models.CharField(max_length=50, choices=NIVELURI_EXPERIENTA, default='INCEPATOR')
    salariu = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"