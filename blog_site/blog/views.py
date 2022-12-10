from django.shortcuts import render, redirect
from . models import posts
from django.contrib import messages
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.utils.text import slugify

from . forms import PostForm
# Create your views here.

class postslist(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4
    
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            title = request.POST.get('title')
         
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(title)
            post.save()
            
            messages.success(request, 'The post was added successfully!')
            
            return redirect('posts')
        else:    
            form = PostForm()     
    
        return render(request, 'post_form.html', {
            'title': 'Add post',
            'form': form
        })    
class postdetail(generic.DetailView):
    model = posts
    template_name = 'postpage.html'
    
