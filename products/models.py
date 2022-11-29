from django.db import models



class Products(models.Model):
    name = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    id = models.PositiveSmallIntegerField(primary_key=True)
    descraption = models.CharField(max_length=1500)
    price = models.IntegerField()
    stack = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now= True)


    def __str__(self):
        return f'{self.name} - {self.stack}'
