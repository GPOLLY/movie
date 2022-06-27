from django.db import models
from datetime import datetime

class SystemUser(models.Model):
    slugId = models.AutoField(primary_key =True)
    firstName =models.CharField(max_length=50, blank = False)
    lastName =models.CharField(max_length=50, blank = False)
    userName =models.CharField(max_length=50, blank = False)
    passWord =models.CharField(max_length=50, blank = False)
    confirmPass =models.CharField(max_length=50, blank = False)
    email =models.EmailField()
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.firstName + ' '+ self.lastName





