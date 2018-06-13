from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from restful.models import File
from django.views import View
from django.core.files.base import ContentFile
from django.middleware import csrf
import requests



def home(request):
    return render(request, 'website/home.html')


@login_required
def file_list(request, path):
	cookies = {'sessionid' : request.session.session_key}
	files = requests.get('http://localhost:8000/restapi/list/'+path, cookies=cookies)
	ret = files.json()
	ret['path'] = path
	return render(request, 'website/file_list.html', ret)

@login_required
def file_upload(request, path):
	file = request.FILES.get('file')
	cookies = {'sessionid' : request.session.session_key}
	cookies['csrftoken'] = csrf.get_token(request)
	headers = {'X-CSRFToken': cookies['csrftoken']}
	requests.post('http://localhost:8000/restapi/list/'+path, files={'file': file}, headers=headers, cookies=cookies)
	return redirect('file_list', path=path)
	
def make_folder(request, path):
	dir_name = request.POST.get('dir_name')
	cookies = {'sessionid' : request.session.session_key}
	cookies['csrftoken'] = csrf.get_token(request)
	headers = {'X-CSRFToken': cookies['csrftoken']}
	print(path)
	files = requests.put('http://localhost:8000/restapi/list/'+path, headers=headers, cookies=cookies)
	return redirect('file_list', path=path)

def file_delete(request, path):
	cookies = {'sessionid' : request.session.session_key}
	cookies['csrftoken'] = csrf.get_token(request)
	headers = {'X-CSRFToken': cookies['csrftoken']}
	requests.delete('http://localhost:8000/restapi/file/'+path, headers=headers, cookies=cookies)
	return redirect('file_list', path="/".join(path.split("/")[:-2]))

def file_download(request, path):
	cookies = {'sessionid' : request.session.session_key}
	requests.get('http://localhost:8000/restapi/file/'+path, cookies=cookies)
	return redirect('file_list', path="/".join(path.split("/")[:-2]))