from django.db import models

# Create your models here.

class ask(models.Model):
    ch = [
        ('js','js'),
        ('python','python'),
        ('C','C'),
    ]
    namee = models.CharField(max_length=20)
    ans = models.CharField(choices=ch, default='js', max_length=20)
    
    def __str__(self) :
        return self.namee