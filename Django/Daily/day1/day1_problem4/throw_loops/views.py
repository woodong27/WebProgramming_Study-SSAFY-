from django.shortcuts import render, redirect

# Create your views here.
def first(request):
    if request.method=="POST":
        throw=request.POST.get('throw')
    else:
        throw='nothing'
    
    context={
        'throw':throw,
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    throw=request.POST.get('throw')
    context={
        'throw':throw,
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    throws=[request.POST.get('throw1'), request.POST.get('throw2')]
    context={
        'throws':throws,
    }
    return render(request, 'throw_loops/third.html', context)