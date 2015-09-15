import json
import re
import urllib2


from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

# Create your views here.
def studies_index(request):
	template = get_template('studies_index.html')

	variables = Context({
			'head_title': 'Studies',
			'page_title': 'Study List',
			'page_body': 'These are the studies',
		})
	output = template.render(variables)
	return HttpResponse(output)

def fetch_study_info(request):
	requestURL = 'http://52.11.158.42:8080/dcm4chee-arc/qido/DCM4CHEE/studies'
	requestURL += '?includefield=all&StudyInstanceUID=' + data

	req = urllib2.Request((requestURL),headers = {'Accept': 'application/json'})
	res = urllib2.urlopen(req)
	return HttpResponse(res.read(), content_type="application/json")
