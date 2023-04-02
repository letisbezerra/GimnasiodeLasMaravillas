from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    
    def __str__(self):
        return "%s %s" % (self.name, self.lastname) 

    class Meta:
        verbose_name_plural = "Instructors"

class Activity(models.Model):
    type=(
        ('Zumba', 'Zumba'),
        ('Pilates', 'Pilates'),
        ('Musculación', 'Musculación'),
        ('Spinning', 'Spinning'),
        ('Funcional', 'Funcional'),
        ('Powerlocal', 'Powerlocal'),
    )
    type = models.CharField(max_length=11, choices=type, default='musculación')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    time = models.TimeField()
    picture = models.ImageField(upload_to="image")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.type 
    
    class Meta:
        verbose_name_plural = "Activities"
    
