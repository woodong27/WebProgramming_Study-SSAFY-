from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    first=int(request.GET.get('first'))
    second=int(request.GET.get('second'))
    mul=first*second
    sub=first-second
    div=0
    if second!=0:
        div=first/second
    context={
        'first':first,
        'second':second,
        'mul':mul,
        'sub':sub,
        'div':div,
    }
    return render(request, 'calculators/result.html', context)