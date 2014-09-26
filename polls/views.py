
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
from polls.models import User
from StringIO import StringIO
import unittest
from polls.tests import allTest



SUCCESS = 1  
ERR_BAD_CREDENTIALS = -1  
ERR_USER_EXISTS = -2  
ERR_BAD_USERNAME = -3  
ERR_BAD_PASSWORD = -4

@csrf_exempt
def login(request):
	if request.method == 'POST':
	    Requestheader = json.loads(request.body)
	    username = Requestheader["user"]
	    password = Requestheader["password"]
	    count_or_code = User.login(username, password)
	    if count_or_code > 0:
		    return HttpResponse(json.dumps({"errCode" : SUCCESS, "count" : count_or_code}), content_type = "application/json")
	    else:
		    return HttpResponse(json.dumps({"errCode" : ERR_BAD_CREDENTIALS, "count" : count_or_code}), content_type = "application/json")

@csrf_exempt
def add(request):
	if request.method == 'POST':
	    Requestheader = json.loads(request.body)
	    username = Requestheader["user"]
	    password = Requestheader["password"]
	    count_or_code = User.add(username, password)
	    if count_or_code > 0:
		    return HttpResponse(json.dumps({"errCode" : SUCCESS, "count" : count_or_code}), content_type = "application/json")
	    else:
		    if count_or_code == ERR_USER_EXISTS:
			    return HttpResponse(json.dumps({"errCode" : ERR_USER_EXISTS, "count" : count_or_code}), content_type = "application/json")
		    if count_or_code == ERR_BAD_USERNAME:
			    return HttpResponse(json.dumps({"errCode" : ERR_BAD_USERNAME, "count" : count_or_code}), content_type = "application/json")
		    else:
			    return HttpResponse(json.dumps({"errCode" : ERR_BAD_PASSWORD, "count" : count_or_code }), content_type = "application/json")

@csrf_exempt
def TESTAPI_resetFixture(request):
	User.TESTAPI_resetFixture()
	return HttpResponse(json.dumps({"errCode" : SUCCESS}), content_type = "application/json")

@csrf_exempt
def TESTAPI_unitTests(request):
	content = StringIO()
	alltests = unittest.TestLoader().loadTestsFromTestCase(allTest)
	msg = unittest.TextTestRunner(stream = content, verbosity=2).run(alltests)
	return HttpResponse(json.dumps({"nrFailed" : len(msg.failures), "output" : content.getvalue(), "totalTests" : msg.testsRun }), content_type = "application/json")








# Create your views here.
