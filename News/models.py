from django.db import models

# Create your models here.
Rank=(
    (1,"Admin"),
    (2,"staff"),
    (3,"CRM"),
)
class Author(models.Model):
    frist_mane = models.CharField(max_length=128)
    Lest_Name = models.CharField(max_length=128)
    rank = models.IntegerField(choices=Rank)
    def __str__(self):
        return self.frist_mane
    
class News(models.Model):
    title = models.CharField(max_length=128)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    content = models.TextField()
    time_date = models.DateTimeField(auto_now_add=True)
    immage = models.ImageField(upload_to="content")
    def __str__(self):
        return self.title
    
    
    
