from django.db import models

Type=(
    ("Apparel","Apparel"),
    ("Footwear","Footwear"),
    ("Accessories","Accessories"),
)

class user_new(models.Model):
    Username = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    

class user_files(models.Model):
    image = models.ImageField(upload_to='user_images')
    gender= models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    occassion=models.CharField(max_length=200)