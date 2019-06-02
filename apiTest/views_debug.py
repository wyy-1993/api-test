from django.shortcuts import render

# Create your views here.
def debug(request):
    return render(request,'./t_debug/debug.html')