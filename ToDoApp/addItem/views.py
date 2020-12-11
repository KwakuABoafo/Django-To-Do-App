from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addItem(request):
    return HttpResponse("This is a test view")

def successfulAddition(request, task):
    return HttpResponse("You successfully added an item to your list for the task: {0}".format(task))