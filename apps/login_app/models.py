from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    
    def createUser(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(username = postData['username'], password = password)

    def loginVal(self, postData):
        results = {'errors': [], 'status': False, 'user': None}
        user_matches = self.filter(username = postData['username'])
        if len(user_matches) == 0:
            results['errors'].append('Please check email and password and try again.')
            results['status'] = True
        else:
            results['user'] = user_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check email and password and try again.')
                results['status'] = True
            return results

    def registerVal(self, postData):
        results = {'errors': [], 'status': False}

        if len(postData['username']) < 2:
            results['status'] = True
            results['errors'].append('Username is too short.')

        if len(postData['password']) < 2:
            results['status'] = True
            results['errors'].append('Password is too short')

        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match')

        user = self.filter(username = postData ['username'])
        
        if len(user) > 0:
            results['status'] = True
            results['errors'].append('Username already exists')

        return results










class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
