# generic API view and mixin

import imp
from .models import StudentModel
from .serializers import studentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
class student_api(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = studentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)





class student_api_pk(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = StudentModel.objects.all()
    serializer_class = studentSerializer

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)