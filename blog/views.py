import re

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

from django.views.generic.edit import FormView
from .forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

def main(request):
    return render(request, 'blog/main.html', {})

def post_i(request): #post_new
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_they')
    else:
        form = PostForm()
    return render(request, 'blog/post_i.html', {'form': form})

def post_you(request):
    return render(request, 'blog/post_you.html', {})

def post_they(request): #post_list
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_they.html', {'posts': posts})

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'
        
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
        q = None
        schLine = '%s' % self.request.POST['search_word']
        schWord = schLine.split()
        for word in schWord:
            q_aux = Q( how__icontains = word ) | Q( when__icontains = word ) | Q( so__icontains = word )
            q = ( q_aux & q ) if bool( q ) else q_aux
        post_list = Post.objects.filter( q )
        
        for word in schWord:
            line1 = post_list[0].how.replace(word,'<b>%s</b>'%(word))
            line2 = post_list[0].when.replace(word,'<b>%s</b>'%(word))   
            line3 = post_list[0].so.replace(word,'<b>%s</b>'%(word))
        
        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list        
        context['line1'] = line1
        context['line2'] = line2
        context['line3'] = line3

                                    
        return render(self.request, self.template_name, context)
