# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def teaching_files_edit(request):
	template = get_template('teaching_files_edit.html')

	variables = Context({
			'head_title': 'Teaching Files',
			'page_title': 'Edit',
			'page_body': 'Edit Teaching File',
		})
	output = template.render(variables)

	return HttpResponse(output)

def teaching_files_index(request):
	template = get_template('teaching_files_index.html')

	variables = Context({
			'head_title': 'Teaching Files',
			'page_title': 'Index',
			'page_body': 'Teaching File',
		})
	output = template.render(variables)

	return HttpResponse(output)