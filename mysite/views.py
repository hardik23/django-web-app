from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template,Context
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,delta):
    offset = int(delta)

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'plus':offset,'dt':dt})
