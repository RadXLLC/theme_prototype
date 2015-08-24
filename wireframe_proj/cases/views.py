from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def cases_index(request):
	template = get_template('cases_index.html')

	variables = Context({
			'head_title': 'Cases',
			'page_title': 'Case List',
			'page_body': 'These are the cases',
		})
	output = template.render(variables)

	return HttpResponse(output)