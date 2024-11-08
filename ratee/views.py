from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from .models import ask
from .serializers import seruser
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
# Create your views here
class ViwSer(viewsets.ModelViewSet):
    queryset = ask.objects.all()
    serializer_class = seruser
def show(request):
    python = 0
    ccc = 0
    jjs = 0
    py = ask.objects.filter(ans = 'python')
    C = ask.objects.filter(ans = 'C')
    JS = ask.objects.filter(ans = 'js')
    for nm in py :
        python += 1
    for nm in C :
        ccc += 1
    for nm in JS :
        jjs += 1
    res = [python, ccc, jjs]
    lab = ['python', 'C', 'js']
    cont = {
        'ress':res,
        'la':lab,
        'pyy': py,
        'c': C,
        'js':JS,
        'np':python,
        'nc':ccc,
        'nj': jjs,
        'ress':res
    }
    return render(request, 'one.html', cont)
@api_view(['GET', 'POST'])
def vot (request):
    if request.method == 'POST':
        dataFromHTML = seruser(data = request.data)
        if dataFromHTML.is_valid():
            dataFromHTML.save()
            return redirect('http://127.0.0.1:8000/home/one')
    return render (request, 'vot.html', {})
