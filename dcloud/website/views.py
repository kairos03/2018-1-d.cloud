from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from restful.models import File
import requests


def home(request):
    return render(request, 'website/home.html')


@login_required
def file_list(request):
    cookies = {'sessionid' : request.session.session_key}
    files = requests.get('http://localhost:8000/restapi/list/', cookies=cookies)
    return render(request, 'website/file_list.html', files.json())
