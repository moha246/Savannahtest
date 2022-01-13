from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.AllhomeView.as_view(), name="home5"),
    path('home5/', views.AllhomeView.as_view(), name="home5"),
    path('about/', views.about, name="about"),
    path('our_team/', views.our_team, name="our_team"),
    path('tataafo/', views.tataafo, name="tataafo"),
    path('fitzone/', views.fitzone, name="fitzone"),
    path('sTrac/', views.sTrac, name="sTrac"),
    path('hacby/', views.hacby, name="hacby"),
    path('contact/', views.contact, name="contact"),
    # path('blog/', views.blog, name="blog"),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path('data_science/', views.data_science, name="data_science"),
    path('software_development/', views.software_development, name="software_development"),
    path('public_health/', views.public_health, name="public_health"),
    # path('blog_list/', views.blog_list, name="blog_list"),


]
app_name = 'Savannah'
