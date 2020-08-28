from django.db import models

# Create your models here.
class Category(models.Model):
    """ A category a user has inside their inventory. """
    text = models.CharField(max_length=32)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """ Return a string representation of the category. """
        return self.text

class Item(models.Model):
    """ Items inside a category. """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    amount = models.IntegerField()
    
    

    def __str__(self):
        """ Return a string representation of the item. """
        return self.name