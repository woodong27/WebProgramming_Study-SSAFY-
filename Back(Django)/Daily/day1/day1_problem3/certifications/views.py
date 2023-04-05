from django.shortcuts import render

# Create your views here.
age=range(25,31)
age=list(map(str,age))
grade=['a','b','c','s']
context={
    'age':age,
    'grade':grade,
}

def certification1(request):
    name='A'
    context['name']=name
    return render(request, 'certifications/certification1.html', context)


def certification2(request):
    name='B'
    context['name']=name
    return render(request, 'certifications/certification2.html', context)


def certification3(request):
    name='C'
    context['name']=name
    return render(request, 'certifications/certification3.html', context)