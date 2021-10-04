from django.db import models

class SignupM(models.Model):
    timestamp = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "signup"

class favouriteM(models.Model):
    timestamp = models.CharField(max_length=50)
    username = models.ForeignKey(SignupM,on_delete=models.CASCADE)
    productid = models.CharField(max_length=50) 
    def __str__(self):
        return self.productid
    
    class Meta:
        db_table = "favourite"

    


