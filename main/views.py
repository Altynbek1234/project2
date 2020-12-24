from django.shortcuts import render
import main.models

from main.models import Phone
# def index(request):
#     lists = [x for x in range(1, 100)]
#     names = ['John', 'Raychel', 'Jane', 'Peter']
#     return render(request, 'index.html', locals())

def get_phone(requests):
    obj_list = main.models.Phone.objects.all()
    return render(requests, 'index.html', locals())


