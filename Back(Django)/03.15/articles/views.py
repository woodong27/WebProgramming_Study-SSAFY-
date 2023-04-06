from django.shortcuts import render

# Create your views here.
def app1(request):
    return render(request, 'articles/app1.html')

def app2(request):
    return render(request, 'articles/app2.html')