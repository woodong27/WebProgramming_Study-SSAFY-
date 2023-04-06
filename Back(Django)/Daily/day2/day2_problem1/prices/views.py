from django.shortcuts import render

# Create your views here.
def index(request,name,cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    
    cost=0
    if name in product_price.keys():
        cost=product_price[name]*cnt
    
    context={
        'product':product_price,
        'name':name,
        'cnt':cnt,
        'cost':cost,
    }
    
    return render(request,'price.html',context)