from django.shortcuts import render
from Auth.models import Users


def home(request):
    user = Users.objects.filter(name=request.session.get('username', 'Guest')).first()
    context = {
        'user': user,
    }
    return render(request, 'Main/home.html', context=context)
