from django.shortcuts import render


def index(request):
    return render(request,'t_case/testCase.html')
