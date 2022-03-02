
from .models import StudentModel
from .serializers import studentSerializer
from rest_framework import viewsets

from api import serializers



class studentViewSet(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class= studentSerializer