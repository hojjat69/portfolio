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
    body = models.CharField(max_length=300)




