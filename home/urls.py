from django.urls import path
from .views import home_page, sitemap_view, robots_view

urlpatterns = [
    path('', home_page),
path('sitemap.xml', sitemap_view),
path('robots.txt', robots_view),
]
