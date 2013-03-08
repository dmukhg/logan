from django.shortcuts import render_to_response
from django.http import HttpResponse

from app.models import Event

def home(request):
  if request.method == 'POST':
    if request.POST.has_key('what') and len(request.POST['what']) > 0:
      e = Event.objects.create(what=request.POST['what'])
      e.save()
    else:
      return HttpResponse('Illegal Request')

  context = {}
  events = Event.objects.all()

  return render_to_response('log.html', {'events': events})
