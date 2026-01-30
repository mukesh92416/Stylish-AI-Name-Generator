from django.shortcuts import render

def home_page(request):
    return render(request, 'home/index.html')
from django.http import HttpResponse
from django.template.loader import render_to_string

def sitemap_view(request):
    xml = render_to_string("home/sitemap.xml")
    return HttpResponse(xml, content_type="application/xml")
def robots_view(request):
    txt = render_to_string("home/robots.txt")
    return HttpResponse(txt, content_type="text/plain")
