from django.db import models

class Budget(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    coming_or_spending = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=False)
    money = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    

