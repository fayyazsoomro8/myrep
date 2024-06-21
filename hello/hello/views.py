from django.shortcuts import render


def index(request):
    return render(request,'index.html')


# def home(request,home):
#     return HttpResponse("Welcome to My Home")