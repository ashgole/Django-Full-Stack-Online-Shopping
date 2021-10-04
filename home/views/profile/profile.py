from home.views.imports import  *

@csrf_exempt
def getProfile(request):
    user=SignupM.objects.get(username=request.session['username_session'])
    context={
        'username':user.username,
        'email':user.email
    }
    return render(request, 'profile/profile.html',context)

@csrf_exempt
def getPutProfile(request,username):
    user=SignupM.objects.get(username=username)
    context={
        'username':user.username,
        'email':user.email
    }
    print(context)
    return render(request, 'profile/edit.html',context)

@csrf_exempt
def putProfile(request):
    u=''
    e=''
    if request.method=='POST':
        u=request.POST['username']
        e=request.POST['email']
        new=SignupM.objects.get(username=request.session['username_session'])
        new.username=u
        new.email=e
        new.save()
        print('*'*20)
        print(new.username)
        print(new.email)
        request.session['username_session'] = new.username
        user=SignupM.objects.get(username=request.session['username_session'])
        context={
            'username':user.username,
            'email':user.email
        }
    return render(request, 'profile/profile.html',context)
