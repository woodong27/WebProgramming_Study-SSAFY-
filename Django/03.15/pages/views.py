from django.shortcuts import render

# Create your views here.
def app1(request):
    return render(request, 'pages/app1.html')