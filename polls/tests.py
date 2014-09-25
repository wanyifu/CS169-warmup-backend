from django.test import TestCase
from polls.models import User

SUCCESS = 1  
ERR_BAD_CREDENTIALS = -1  
ERR_USER_EXISTS = -2  
ERR_BAD_USERNAME = -3  
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class allTest(TestCase):
	def build_account(self):
		a = User().add("wanyifu11", password = "felix11")
		b = User().add("wanyifu12", password = "felix12")
		c = User().add("wanyifu13", password = "felix13")
		d = User().add("wanyifu14", password = "felix14")
        self.assertEqual(SUCCESS,a)
        self.assertEqual(SUCCESS,b)
        self.assertEqual(SUCCESS,c)
        self.assertEqual(SUCCESS,d)


	def login_auth(self):
		self.assertEqual(User().login("wanyifu11","hello"), ERR_BAD_CREDENTIALS)
		self.assertEqual(User().login("wanyifu11","felix14"),ERR_BAD_CREDENTIALS)
		self.assertEqual(User().login("wanyifu13","felix13"),SUCCESS)
		self.assertEqual(User().login("wanyifu15","felix13"),ERR_BAD_CREDENTIALS)

	def login_count(self):
		a = User().login("wanyifu1","felix1")
		b = User().login("wanyifu1","felix1")
		c = User().login("wanyifu2","felix2")
		d = User().login("wanyifu3","felix3")
        e = User().login("wanyifu4","felix4")
        self.assertEqual(a,1)
        self.assertEqual(b,2)
        self.assertEqual(c,1)
        self.assertEqual(d,1)
        self.assertEqual(e,1)

    def add_pw_long_invalid(self):
    	self.assertEqual(User().add("wanyifu5","felix5"*21),SUCCESS)
    	self.assertEqual(User().add("wanyifu6","felix5"*22),ERR_BAD_PASSWORD)

    def add_pw_none_valid(self):
    	self.assertEqual(User().add("wanyifu7"," "),SUCCESS)

    def add_um_long_invalid(self):
    	self.assertEqual(User().add("a"*127,"felix8"),SUCCESS)
    	self.assertEqual(User().add("a"*129,"felix9"),ERR_BAD_USERNAME)

    def add_um_none_invalid(self):
    	self.assertEqual(User().add(" ","felix10"),ERR_BAD_USERNAME)

    def add_repeated_invalid(self):
    	self.assertEqual(User().add("wanyifu1","felix11"),ERR_USER_EXISTS)

    def resetfix(self):
    	self.assertEqual(User().TESTAPI_resetFixture(),SUCCESS)















# Create your tests here.
