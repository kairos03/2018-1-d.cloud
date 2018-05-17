from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from website.models import Post
from restful.models import File



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/post_list.html', {'posts':posts})

def file_list(request):
    files = File.objects.all()
    return render(request, 'website/file_list.html', {'files': files})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/post_detail.html', {'post': post})
