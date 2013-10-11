from django.http import HttpResponse
import datetime


def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>hello world<p>It is now %s. </p></body></html>" % now
	return HttpResponse(html)