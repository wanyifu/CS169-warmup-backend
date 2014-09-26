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
    def test_build_account(self):
        a = User().add("wanyifu11", "felix11")
        b = User().add("wanyifu12", "felix12")
        c = User().add("wanyifu13", "felix13")
        d = User().add("wanyifu14", "felix14")
        self.assertEqual(SUCCESS,a)
        self.assertEqual(SUCCESS,b)
        self.assertEqual(SUCCESS,c)
        self.assertEqual(SUCCESS,d)


    def test_ogin_auth(self):
        self.assertEqual(User().login("wanyifu11","hello"), ERR_BAD_CREDENTIALS)
        self.assertEqual(User().login("wanyifu11","felix14"),ERR_BAD_CREDENTIALS)
        self.assertEqual(User().login("wanyifu15","felix13"),ERR_BAD_CREDENTIALS)

    def test_login_count(self):
        a = User().add("wanyifu1", "felix1")
        b = User().add("wanyifu2", "felix2")
        c = User().add("wanyifu3", "felix3")
        d = User().add("wanyifu4", "felix4")
        e = User().login("wanyifu1","felix1")
        f = User().login("wanyifu1","felix1")
        g = User().login("wanyifu2","felix2")
        h = User().login("wanyifu3","felix3")
        i = User().login("wanyifu4","felix4")
        self.assertEqual(e,2)
        self.assertEqual(f,3)
        self.assertEqual(g,2)
        self.assertEqual(h,2)
        self.assertEqual(i,2)

    def test_add_pw_long_invalid(self):
        self.assertEqual(User().add("wanyifu5","felix5"*21),SUCCESS)
        self.assertEqual(User().add("wanyifu6","felix5"*22),ERR_BAD_PASSWORD)

    def test_add_pw_none_valid(self):
        self.assertEqual(User().add("wanyifu7"," "),SUCCESS)

    def test_add_um_long_invalid(self):
        self.assertEqual(User().add("a"*127,"felix8"),SUCCESS)
        self.assertEqual(User().add("a"*129,"felix9"),ERR_BAD_USERNAME)

    def test_add_um_none_invalid(self):
        self.assertEqual(User().add(" ","felix10"),SUCCESS)

    def test_add_repeated_invalid(self):
        a = User().add("wanyifu16", "felix16")
        self.assertEqual(User().add("wanyifu16","felix17"),ERR_USER_EXISTS)

    def test_resetfix(self):
        self.assertEqual(User().TESTAPI_resetFixture(),SUCCESS)















# Create your tests here.
