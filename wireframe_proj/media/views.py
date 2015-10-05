from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

# Create your views here.
# Create your views here.
def media_index(request):
	template = get_template('media_index.html')

	variables = Context({
			'head_title': 'Media',
			'page_title': 'Media List',
			'page_body': 'These are the Media',
		})
	output = template.render(variables)
	return HttpResponse(output)
