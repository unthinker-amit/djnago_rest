from functools import partial
import imp
from django.shortcuts import render
from api.models import StudentModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import studentSerializer

# Create your views here.
# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method=="GET":
#         return Response({'data':request.data,'msg':'hello this is the post'}) 
#     if request.method=="POST":
#         return Response({'data':request.data,'msg':'hello this is the post'}) 


@api_view(['GET',"POST","PUT","PATCH","DELETE"])
def student_api(request,pk=None):
    if request.method=="GET":
        id =pk
        if id is not None:
            stu = StudentModel.objects.get(id=id)
            serializer=studentSerializer(stu)
            return Response(serializer.data)
        stu=StudentModel.objects.all()
        serializer=studentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method=="POST":
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"data created"})
        return Response(serializer.errors)
    
    if request.method=="PUT":
        id=pk
        stu=StudentModel.objects.get(pk=id)
        serializer=studentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"data updated"})
        return Response(serializer.errors)

    if request.method=="PATCH":
        id=pk
        stu=StudentModel.objects.get(pk=id)
        serializer=studentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"data updated"})
        return Response(serializer.errors)
        
    if request.method=="DELETE":
        id=pk
        stu=StudentModel.objects.get(pk=id)
        stu.delete()
        return Response({"data":"data deleted"})
