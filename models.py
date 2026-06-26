from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



# Create your models here.
class BasicDetails(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    photo= models.ImageField(upload_to='photo/')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_created=True)
    
class Course(models.Model):
    title= models.CharField(max_length=100)
    description=models.DurationField(blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.name
class Mentor(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    courses= models.ManyToManyField(Course, related_name='mentor')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_created=True)
    
class Batch(models.Model):
    course= models.ForeignKey(Course, on_delete=models.CASCADE)
    # mentor= models.OneToOneField(Mentor, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)    
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_created=True)
class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    text = CKEditor5Field('Text', config_name='extends')    
    
