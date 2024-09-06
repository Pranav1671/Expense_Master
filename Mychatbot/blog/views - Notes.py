from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is my first URL")  #http://127.0.0.1:8000/blog/
    '''
    return render(request, 'blog/index.html')
    '''

def specific(request):
    return HttpResponse("This is a specific URL")  #http://127.0.0.1:8000/blog/specific

def returndatas(request):
    number = 66
    list1 = [1,2,3,4,5]
    return HttpResponse(number)     #http://127.0.0.1:8000/blog/returndatas
    #return HttpResponse(list1)

def article(request,article_id):
    return HttpResponse(article_id)   

    '''
    http://127.0.0.1:8000/blog/article/20
    http://127.0.0.1:8000/blog/article/1000
    http://127.0.0.1:8000/blog/article/765
    '''

def article2(request,article_id):
    return render(request, 'blog/index.html',{'article_id':article_id}) 


def new(request):
    return render(request, 'blog/index.html')