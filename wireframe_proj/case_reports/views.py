from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def case_reports_edit(request):
	template = get_template('case_reports_edit.html')

	variables = Context({
			'head_title': 'Case Reports',
			'page_title': 'Edit',
			'page_body': 'Edit Case Report',
		})
	output = template.render(variables)

	return HttpResponse(output)

def case_reports_index(request):
	template = get_template('case_reports_index.html')

	variables = Context({
			'head_title': 'Case Reports',
			'page_title': 'Edit',
			'page_body': 'Edit Case Report',
		})
	output = template.render(variables)

	return HttpResponse(output)