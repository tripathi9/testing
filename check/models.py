from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.


class Profile(models.Model):
   first_name = models.CharField(('first name'),max_length=50,blank=False,default='')
   last_name = models.CharField(('Last name'),max_length=50,blank=True,default='')
   avatar = models.ImageField(null=True, blank=True, max_length=5000)
   mobile = models.CharField(('Mobile'),max_length=10,blank=True,unique=False)
   city = models.CharField(('City'),max_length=50,blank=False)
   state  = models.CharField(('State'),max_length=50,blank=False,default='')
   country = models.CharField(('Country'),max_length=50,blank=False,default='')
   created_at = models.DateTimeField(('created_at'),auto_now = True)
   updated_at = models.DateTimeField(('updated_at'),auto_now = True)
   userid=models.ForeignKey(User, on_delete=models.CASCADE)



class Event(models.Model):
    event_name = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)
    event_date = models.DateField(auto_now_add=False)
    address = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})
# class Event_Attendies(models.Model):
#     attendiesid = models.ForeignKey(User, on_delete=models.CASCADE)
#     eventid = models.ForeignKey(Event, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)
