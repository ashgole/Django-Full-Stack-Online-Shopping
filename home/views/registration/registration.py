from home.views.imports import *

def signin(request):
    return render(request, 'registration/signin.html')

def signup(request):
    return render(request, 'registration/signup.html')

@csrf_exempt
def postSignin(request):
    try:
        if request.method == 'POST':
            print('post**'*10)
            username=request.POST.get('username',False)
            password=request.POST.get('password',False)
            request.session['username_session'] = username
            print(username, password)
            isvalid=SignupM.objects.filter(username=username,password=password).exists()
            print(isvalid)
            if isvalid:
                return render(request, 'index.html', productsContext)
            else:
                return HttpResponse('Username or Password is wrong')    
    except Exception as e:
        print("An exception occurred: ", e)   
        return HttpResponse('something went wrong')

 

