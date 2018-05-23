from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from website.models import Post
from restful.models import File
from website.forms import PostForm

@login_required
def file_list(request):
    files = File.objects.all()
    return render(request, 'website/file_list.html', {'files': files})
