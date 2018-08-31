import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.debug import ( 
								sensitive_variables, 
								sensitive_post_parameters
									)

from server.models import Profile


@sensitive_variables('phone_number', 'passport_number')
def getUserProfile(request):
	data = {
		'phone_number':str(request.user.profile.phone_number),
		'passport_number':request.user.profile.passport_number
	}
	return HttpResponse(json.dumps(data), content_type="application/json")


@sensitive_post_parameters('phone_number', 'passport_number')
def updateUserProfile():
	profile = request.user.profile
	profile.phone_number = request.POST['phone_number']
	profile.passport_number = request.POST['passport_number']
	profile.save()
	return HttpResponse("+OK")
