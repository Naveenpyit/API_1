from .models import clgstudent,clgcourses
from rest_framework.serializers import ModelSerializer

class clgserializer(ModelSerializer):
    class Meta:
        model=clgstudent
        fields='__all__'

class courseserializer(ModelSerializer):
    class Meta:
        model=clgcourses
        fields='__all__'        