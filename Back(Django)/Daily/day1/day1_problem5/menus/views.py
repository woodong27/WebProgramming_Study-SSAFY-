from django.shortcuts import render

# Create your views here.
foods=['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
drinks=['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']

def food(request):
    context={
        'foods':foods,
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    context={
        'drinks':drinks,
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    order=request.POST.get('order')
    context={
        'order':order,
    }
    if order in foods or order.lower() in drinks:
        context['valid']=True  
    else:
        context['valid']=False
        
    return render(request, 'menus/receipt.html', context)