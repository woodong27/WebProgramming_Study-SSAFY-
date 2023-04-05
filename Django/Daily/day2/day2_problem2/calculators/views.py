from django.shortcuts import render

# Create your views here.
def calculator(request, first, second):
    div=0
    if second!=0:
        div=first/second
    
    context={
        'first':first,
        'second':second,
        'mul':first*second,
        'sub':first-second,
        'div':div,
    }

    return render(request,'calculators/calculator.html', context)