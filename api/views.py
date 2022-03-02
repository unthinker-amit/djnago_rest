import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def hello_world(request):
    if request.method=="GET":
        return Response({'data':request.data,'msg':'hello this is the post'}) 
    if request.method=="POST":
        return Response({'data':request.data,'msg':'hello this is the post'}) 