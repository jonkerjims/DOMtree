from django.shortcuts import render

# Create your views here.
def showIndex(request,name,music,icon):
    print(name,music,icon)
    return render(request,'NewYear/index.html')