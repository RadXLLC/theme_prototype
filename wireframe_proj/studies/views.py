from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

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