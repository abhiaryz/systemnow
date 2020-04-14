from django.db import models

# Create your models here.
class Server(models.Model):
    name = models.CharField('server name', max_length=40)
    platform = models.CharField('server platform', max_length=200)



class Website(models.Model):
    name= models.CharField('website name', max_length=40)
    location= models.CharField('website location', max_length=40)
    interval= models.CharField('website interval', max_length=50)
    url= models.CharField('website url',max_length=100)
    last_checked_time = models.CharField('website lastchecked', max_length=100,default='')
    loadtime = models.CharField('website loadtime', max_length=5,default='')
    uptime = models.CharField('website uptime', max_length=5,default='')

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField('user fname', max_length=40)
    last_name = models.CharField('user fname', max_length=40)
    address = models.CharField('user address', max_length=200)
    mobile = models.IntegerField('user mobile ', max_length=10)
    email = models.CharField('user email', max_length=60)
    organisation = models.CharField('user organisation', max_length=100)
    desgination = models.CharField('user designation', max_length=50)

