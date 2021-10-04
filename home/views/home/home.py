from home.views.imports import *


@csrf_exempt
def home(request):
    print('*'*20)
    try:
        if request.method == 'POST':
            print('post**'*10)
            username=request.POST.get('username',False)
            email=request.POST.get('email',False)
            password=request.POST.get('password',False)
            request.session['username_session'] = username
            print(request.session['username_session'])
            print(username, email, password)
            insert=SignupM.objects.create(timestamp=datetime.now,username=username,email=email,password=password)
            insert.save()
    except Exception as e:
        print("An exception occurred: ", e)
    return render(request, 'index.html', productsContext)


def getProduct(request,id):
    context ={}
    for i in productsContext['products']:
        if i['id'] == id:
            context=i
    return render(request, 'home/product.html',context)

#FIXME after clicking on add to fav showing http://127.0.0.1:8000/postcart/
@csrf_exempt
def postCart(request):
    print('*'*20)
    print(request)
    if request.method =='POST':
        un=request.session['username_session']
        uname = SignupM.objects.get(username=un)
        productid=request.POST.get('productid',False)
        insert=favouriteM.objects.create(username=uname,timestamp=datetime.now,productid=str(productid))
        insert.save()
    return render(request, 'index.html', productsContext)

@csrf_exempt
def postBuy(request):
    print('*'*20)
    print(request)
    # if request.method =='POST':
    #     un=request.session['username_session']
    #     uname = SignupM.objects.get(username=un)
    #     x=request.POST.get('myid',False)
    #     print('product id {} buy'.format(x))
    return render(request, 'home/buy.html',)
