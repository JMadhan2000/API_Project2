from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.models import *

class ProductDetails(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        JDO=ProductModelSerializer(PDO,many=True)
        return Response(JDO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'value':'Data Inserted Successfully....'})
        else:
            return Response({'Error':'Data not Inserted...'})