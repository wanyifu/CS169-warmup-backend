from django.db import models

SUCCESS = 1  
ERR_BAD_CREDENTIALS = -1  
ERR_USER_EXISTS = -2  
ERR_BAD_USERNAME = -3  
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = MAX_USERNAME_LENGTH)
    password = models.CharField(max_length = MAX_PASSWORD_LENGTH)
    count = models.IntegerField()

    @classmethod
    def login(self,input_username,input_password):
        try:
            userinfo = User.objects.get(username = input_username)
            if userinfo.password == input_password:
                userinfo.count += 1
                userinfo.save()
                return userinfo.count
            else:
                return ERR_BAD_CREDENTIALS
        except:
            return ERR_BAD_CREDENTIALS

    @classmethod
    def add(self,new_username,new_password):
        try:
            userinfo = User.objects.get(username = new_username)
            return ERR_USER_EXISTS
        except:
            if len(new_username) == 0 or len(new_username) > MAX_USERNAME_LENGTH:
                return ERR_BAD_USERNAME
            if len(new_password) > MAX_PASSWORD_LENGTH:
                return ERR_BAD_PASSWORD
            else:
                added_user = User(username = new_username, password = new_password, count = 1)
                added_user.save()
                return added_user.count

    @classmethod
    def TESTAPI_resetFixture(self):
        User.objects.all().delete()
        return SUCCESS












