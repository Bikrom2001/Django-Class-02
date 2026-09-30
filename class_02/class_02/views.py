from django.http import HttpResponse

def home_page(request):
    
    return HttpResponse('Hello, World')


def about_page(request):
    
    return HttpResponse('About page')