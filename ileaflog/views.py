__author__ = 'remillet'

from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    return render_to_response('ileaflog/index.html')

def oauth(request):
    print "Code = " + request.GET.__getitem__('code')
    return render_to_response('ileaflog/oauth.html')
