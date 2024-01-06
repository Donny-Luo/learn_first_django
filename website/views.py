from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'D:\Learn_Coding\Pythone_Project\l_django\django_crm\dcrm\website\templates\home.html', {})