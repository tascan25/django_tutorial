from datetime import date
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Author
from django.views.generic.edit import CreateView
from django.views import View
from .forms import BlogEntryForm
from .models import Post, Author
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .models import CommentModel

# post = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Maximilian",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Maximilian",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Maximilian",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]

# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "latestPosts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data
    
class PostListView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "allPosts"


class PostDetailView(View):
    def get(self,request,slug):
        extracted_post = Post.objects.get(slug=slug)
        form = CommentForm()
        return render(request,"blog/post-detail.html",{
            "detailedPost":extracted_post,
            "form":form, 
            "comments":extracted_post.comments.all().order_by("-id")
        })
    
    def post(self,request,slug):
        form = CommentForm(request.POST)
        extracted_post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = extracted_post
            comment.save()
            return HttpResponseRedirect(reverse('posts_detail_page',args=[slug]))
           
        return render(request,"blog/post-detail.html",{
            "detailedPost":extracted_post,
            "form":form,
            "comments":extracted_post.comments.all().order_by("-id")
        })



class BlogEntryView(View):
    def get(self,request):
        form = BlogEntryForm()
        return render(request, "blog/blog_entry.html",{
            "form":form
        })
    
    def post(self,request):
        form = BlogEntryForm(request.POST,request.FILES)

        if form.is_valid():

            author, created = Author.objects.get_or_create(
            email_address=form.cleaned_data['author_email'],  # email is unique enough to match on
            defaults={
            'first_name': form.cleaned_data['author_first_name'],
            'last_name': form.cleaned_data['author_last_name'],
            }
            )
            new_post = Post(
                title=form.cleaned_data['title'],
                excerpt=form.cleaned_data['excerpt'],
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                author=author,
                slug = slugify(form.cleaned_data['title'])
            )

            new_post.save()

            # because we need to set the many to many field, once the object is created
            new_post.tag.set(form.cleaned_data['tag'])
            return HttpResponseRedirect('/posts/')
        return render(request, "blog/blog_entry.html",{
            "form":form
        })
    
class ReadLaterView(View):

    def get(self,request):
        stored_post = request.session.get("stored_posts")
        context = {}
        if stored_post is None or len(stored_post)==0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in = stored_post)
            context['has_posts'] = True
            context['posts']=posts 
        return render(request,'blog/stored_post.html',context)
    def post(self,request):
        stored_post = request.session.get("stored_posts")

        if stored_post is None:
            stored_post = []
        post_id = int(request.POST["post_id"])
        if post_id not in stored_post:
            stored_post.append(post_id)
            request.session["stored_posts"] = stored_post
        return HttpResponseRedirect("/")

    
# def starting_page(request):
#     latest_post_arr = Post.objects.all().order_by("-date")[:3]
#     return render(request, 'blog/index.html',{
#         "latestPosts": latest_post_arr
#     })

# def posts(request):
#     post_arr = Post.objects.all()
#     return render(request,'blog/all-posts.html',{
#         "allPosts": post_arr
#     })

# def posts_detail(request,slug):
#     detailed_post = get_object_or_404(Post, slug=slug)
#     # find_post = next((item for item in post if item["slug"]==slug),None)
#     # print(find_post)
#     return render(request,'blog/post-detail.html',{
#         "detailedPost": detailed_post,
#         "authoremail":detailed_post.author.email_address
#     })
