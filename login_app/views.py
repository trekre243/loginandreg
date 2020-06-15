from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import User
import bcrypt

def login(request):
    return render(request, 'login.html')

def check_login(request):
    try:
        user = User.objects.get(email=request.POST['email'])
    except:
        messages.error(request, 'Not a valid email address')
        return redirect('/')
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['id'] = user.id
        request.session.save()
        return redirect('/success')
    else:
        messages.error(request, 'Incorrect password')
        return redirect('/')

def register(request):
    errors =User.objects.user_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        hash_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(fname=fname, lname=lname, password=hash_pass, email=email)
        request.session['id'] = user.id
        request.session.save()
        return redirect('/success')

def success(request):
    if 'id' not in request.session:
        return redirect('/')
    print(request.session['id'])
    user = User.objects.get(id=request.session['id'])
    context = {
        'fname': user.fname
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')