from django.urls import path
from .views import index, post_detail, get_ip, post_table

app_name="blog"

urlpatterns = [
  path("", index, name="index"),
  path("post/<slug>/", post_detail, name="blog-post-detail"),
  path("ip/", get_ip),
  path("post-table/", post_table, name="blog-post-table"),

]