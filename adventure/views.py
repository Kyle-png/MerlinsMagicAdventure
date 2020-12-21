from django.shortcuts import render
from django.http import HttpResponse
import requests
# from adventure.models import character



#theChar = character()

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
    #return HttpResponse('<html><title>To-Do lists</title></html>')

# if __name__ == '__main__':
#     #if calls the class if it is not instantiated elsewhere
#     theChar = character("","","")