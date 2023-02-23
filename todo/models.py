from django.db import models

# Create your models here.


# Analagous to a DB Table
# NULL = FALSE MEANS ANY ITEM WITHOUT A NAME WILL NOT BE CREATED
# Blank = False makes the field a required field
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)


# Overides defualt name from inherited models class, changes it to actual name

    def __str__(self):
        return self.name
