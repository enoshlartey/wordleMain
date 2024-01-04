from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'homeApp/index.html')

def selectView(request):
    return render(request, 'homeApp/selection.html')