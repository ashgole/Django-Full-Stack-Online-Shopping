from home.views.imports import *
import smtplib
from random import randint

def forget(request):
    gmail_user = 'myemail@gmail.com'  #use your email
    gmail_password = '<google-app-password>' #create password using google app password
    otp=randint(999,9999)
    request.session['otp'] = str(otp)
    sent_from = gmail_user
    to = ['myemail@gmail.com']
    subject = 'OMG Super Important Message'
    message = 'your OTP is '+ str(otp)
    # message.format(gmail_user=gmail_user,to=to,sub='SMTP e-mail test')

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg=message)

        print('Email sent!')
    except:
        print('Something went wrong...')
    return render(request, 'registration/forget.html',)

@csrf_exempt
def setPassword(request):
    try:
        if request.method=='POST':
            otp=request.POST['otp']
            username=request.POST['username']
            newpassword=request.POST['newpassword']
        if otp == request.session['otp']:
            user=SignupM.objects.get(username=username)
            user.password=newpassword
            user.save()
            request.session['username_session'] = username
            return render(request, 'index.html',)
        else:
            return HttpResponse('wrong OTP',)
    except:
        return HttpResponse('something went wrong',)
