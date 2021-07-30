from django.shortcuts import render
from django.shortcuts import HttpResponse

def Welcome(request):
    return HttpResponse('Welcome')

def HomePage(request):
    user_name = request.GET.get('user_name')
    user_password = request.GET.get('user_password')
    fullname = f"User_Name : {user_name} Password : {user_password}"
    data = {'fullname' : fullname}
    return render(request, 'Home.html', data )