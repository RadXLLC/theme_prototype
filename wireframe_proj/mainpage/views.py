from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
	template = get_template('main_page.html')

	variables = Context({
			'head_title': 'Wireframe 2',
			'page_title': 'Welcome to the Wireframe Project 2',
			'page_body': 'This is the start of the Wireframe Project 2',
		})
	output = template.render(variables)

	return HttpResponse(output)


