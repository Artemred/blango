from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
import logging
logger = logging.getLogger(__name__)


def index(request):
    posts = (
      Post.objects.all()
      .select_related("author")
      .defer("created_at", "modified_at")
    )
    logger.debug("Got %d posts", len(posts))
    return render(request, "index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
)
    return render(request, "post-detail.html", {"post": post, "comment_form":comment_form})

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])