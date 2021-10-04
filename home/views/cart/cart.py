from home.views.imports import *

@csrf_exempt
def getCart(request): 
    try:
        print('*'*20) 
        uns=request.session['username_session']
        username = SignupM.objects.get(username=uns) 
        istrue=favouriteM.objects.filter(username=username).count()
        if istrue >= 1:
            favidList=[]
            total=0         
            getcart=favouriteM.objects.filter(username=username).values('productid') 
            for i in productsContext['products']: 
                if i['id'] in [str(i['productid']) for i in getcart]:
                    total+=int(i['price'])
                    favidList.append(i['id'])

            productsContext['favidList']=favidList         
            productsContext['total']=total         
            return render(request, 'cart/cart.html',productsContext)
        else:
            return render(request, 'cart/empty.html')
    except Exception as e:
        print("An exception occurred: ", e)
        return HttpResponse(e)       

@csrf_exempt
def deleteCart(request):
    try:
        print('*'*20)         
        uns=request.session['username_session']
        username = SignupM.objects.get(username=uns)
        productid=request.POST.get('productid',False)
        print('username ',username)
        print('productid ',productid)
        favouriteM.objects.filter(username=username,productid=productid).delete() 
        istrue=favouriteM.objects.filter(username=username).count()
        if istrue >= 1:
            favidList=[]             
            getcart=favouriteM.objects.filter(username=username).values('productid')
            for i in getcart:
                favidList.append(i['productid']) 
            print(favidList) 
            productsContext['favidList']=favidList    
            return render(request, 'cart/cart.html',productsContext)
        else:
            return render(request, 'cart/empty.html')
    except Exception as e:
        print("An exception occurred: ", e)
        return HttpResponse(e)  