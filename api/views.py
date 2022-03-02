# generic API view and mixin

import imp
from .models import StudentModel
from .serializers import studentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class student_api(ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = studentSerializer




class student_api_RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = studentSerializer

    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.delete(request,*args,**kwargs)