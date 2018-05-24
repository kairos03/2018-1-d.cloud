from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from restful.models import File
import requests


def home(request):
    return render(request, 'website/home.html')


@login_required
def file_list(request):
    files = requests.get('http://localhost:8000/restapi/files')
    files = files.json()
    return render(request, 'website/file_list.html', files)
