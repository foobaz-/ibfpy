from django.http import HttpResponse
from ibf.models import Users
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response

def list_users(request):
  args = {'users': Users.objects.all()}
  ctx = RequestContext(request)
  return render_to_response( 'list_users.html'
                           , args
                           , ctx )

