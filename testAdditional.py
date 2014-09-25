import unittest
import os
import testLib

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1 
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class Test_Suites(testLib.RestTestCase):

	def test_add(self):
		r1 = self.makeRequest("/users/add", method="POST", data = {'user':'u1','password':'p1'} )
		r2 = self.makeRequest("/users/add", method="POST", data = {'user':'u2','password':'p2'} )
		self.assertEqual(r1['errCode'], SUCCESS)
		self.assertEqual(r2['errCode'], SUCCESS)
		self.assertEqual(r1['count'], 1)
		self.assertEqual(r2['count'], 1)

	def test_add_exist(self):
		r3 = self.makeRequest("/users/add", method="POST", data = {'user':'u3','password':'p3'} )
		e1 = self.makeRequest("/users/add", method="POST", data = {'user':'u3','password':'p3'} )
		self.assertEqual(e1['errCode'],ERR_USER_EXISTS)

	def test_add_long_user(self):
		long_user = 'eu1'*100
		e2 = self.makeRequest("/users/add", method="POST", data = {'user':long_user,'password':'p3'} )
		self.assertEqual(e2['errCode'],ERR_BAD_USERNAME)

	def test_add_long_pw(self):
		long_pw = 'ep1'*100
		e3 = self.makeRequest("/users/add", method="POST", data = {'user':'u4','password':long_pw} )
		self.assertEqual(e3['errCode'],ERR_BAD_PASSWORD)




	def test_login_count(self):
		r5 = self.makeRequest("/users/add", method="POST", data = {'user':'u5','password':'p5'} )
		r51 = self.makeRequest("/users/login", method="POST", data = {'user':'u5','password':'p5'} )
		r52 = self.makeRequest("/users/login", method="POST", data = {'user':'u5','password':'p5'} )
		r52 = self.makeRequest("/users/login", method="POST", data = {'user':'u5','password':'p5'} )
		self.assertEqual(r51['count'],1)
		self.assertEqual(r52['count'],2)
		self.assertEqual(r53['count'],3)

	def test_login_basic(self):
		r6 = self.makeRequest("/users/add", method="POST", data = {'user':'u6','password':'p6'} )
		e4 = self.makeRequest("/users/login", method="POST", data = {'user':'u6','password':'p7'} )
		e5 = self.makeRequest("/users/login", method="POST", data = {'user':'u7','password':'p6'} )
		self.assertEqual(e4['errCode'], ERR_BAD_CREDENTIALS)
		self.assertEqual(e5['errCode'], ERR_BAD_CREDENTIALS)

	def test_reset(self):
		r8 = self.makeRequest("/users/add", method="POST", data = {'user':'u8','password':'p8'} )
		r9 = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {} )
		r10 = self.makeRequest("/users/login", method="POST", data = {'user':'u8','password':'p8'} )
		self.assertEqual(r10['errCode'], ERR_BAD_CREDENTIALS)












