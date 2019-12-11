from django.db import models
# Create your models here.

# It needs to have a title, pub date, body, image 

# create a bolg model

# add the blog app to the setting

# create a migration 

# migrate

# add to the admin


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title =models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=10000)

    def summary (self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y ')
    def __str__(self):
        return self.title    
        




