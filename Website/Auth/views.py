from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import Users
from django.template.defaultfilters import slugify
import re


def login(request):
    return render(request, 'Auth/login.html')


def signup(request):
    return render(request, 'Auth/signup.html')


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")


def login_verify(request):
    data = {
        'common': ' | ',
    }
    status = 200
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # username,email,password fields does not filled up
        if len(username) == 0:
            data['common'] += '⚠ user name field is empty | '
            status = 406
        if len(password) == 0:
            data['common'] += '⚠ password field is empty | '
            status = 406
        # Check if user already exist
        required_user = Users.objects.filter(name=username)
        if required_user.exists():
            # Password does match
            if required_user.first().password == password:
                status = 200
                request.session["is_auth"] = True
                request.session["username"] = username
                data['common'] = '✔ You have successfully sign in, redirecting ... '
            else:
                data['common'] = '⚠ Wrong password'
                status = 406
        else:
            data['common'] = '⚠ No such user in database'
            status = 406

        return JsonResponse(data, status=status)


def signup_verify(request):
    data = {
        'common': ' | '
    }
    status = 200
    if request.method == 'POST':
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeated_password = request.POST['repassword']
        if len(username) == 0:
            data['common'] += '⚠ user field is empty | '
            status = 406
        if len(email) == 0:
            data['common'] += '⚠ email is empty | '
            status = 406
        if len(password) == 0:
            data['common'] += '⚠ password is empty | '
            status = 406
        # Check if user already exist
        if Users.objects.filter(name=username).exists() or Users.objects.filter(slug=slugify(username)).exists():
            data['common'] += '⚠ user with such name already exist | '
            status = 406
        # Check if email already used
        if Users.objects.filter(email=email).exists():
            data['common'] += '⚠ this email already in use | '
            status = 406
        # Check if username's length is big enough
        if len(username) < 3:
            data['common'] += '⚠ too short user name | '
            status = 406
        # Check if username's length not to big
        if len(username) > 25:
            data['common'] += '⚠ too long user name | '
            status = 406
        # Check if password length is big enough
        if len(password) < 6:
            data['common'] += '⚠ too short password | '
            status = 406
        # Password does not match
        if password != repeated_password:
            data['common'] += '⚠ passwords mismatch | '
            status = 406
        # Email addres does not right
        if not re.fullmatch(regex, email):
            data['common'] += '⚠ email formant are not correct | '
            status = 406
        if status == 200:
            data['common'] = '✔ you have successfully sign up | '
            user = Users(name=username, email=email, password=password)
            user.save()

        return JsonResponse(data, status=status)
    else:
        status = 403
        data['common'] = "Allowed only POST request"
        return JsonResponse(data, status=status)
