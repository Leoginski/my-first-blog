from django.shortcuts import render
from django.template import RequestContext 


def post_list(request):
    return render(request, 'blog/post_list.html', {})