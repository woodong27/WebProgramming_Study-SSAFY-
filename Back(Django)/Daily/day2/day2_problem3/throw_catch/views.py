from django.shortcuts import render

# Create your views here.
def first(request):
    catch=0
    if request.method=='POST':
        catch=request.POST.get('throw')
    
    context={
        'catch':catch,
    }
    
    return render(request, 'throw_catch/first.html', context)

def second(request):
    catch=request.POST.get('throw')
    context={
        'catch':catch,
    }
    
    return render(request, 'throw_catch/second.html', context)