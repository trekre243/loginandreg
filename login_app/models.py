from django.db import models
import re

class UserManager(models.Manager):
    def user_validate(self, postData):
        
        errors = {}

        if len(postData['fname']) < 2:
            errors['fname'] = 'First name must be at least 2 characters'

        if len(postData['lname']) < 2:
            errors['lname'] = 'Last name must be at least 2 characters'

        if not re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', postData['email']):
            errors['email'] = 'Email address is an invalid format'

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['cpassword']:
            errors['password'] = 'Password and confirmation password must match'
        
        return errors


class User(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()