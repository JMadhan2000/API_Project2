from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

class ProductDetails(APIView):
    def get(self,request,id):
        PDO=Product.objects.all()
        JDO=ProductModelSerializer(PDO,many=True)
        #PDO=Product.objects.get(Product_id=id)
        #JDO=ProductModelSerializer(PDO)
        return Response(JDO.data)
    
    def post(self,request,id):
        PDO=request.data
        JDO=ProductModelSerializer(data=PDO)
        if JDO.is_valid():
            JDO.save()
            return Response({'value':'Data Inserted Successfully....'})
        else:
            return Response({'Error':'Data not Inserted...'})
        
    def put(self,request,id):
        PO=Product.objects.get(Product_id=id)
        JDO=ProductModelSerializer(PO,data=request.data)
        if JDO.is_valid():
            JDO.save()
            return Response({'value':'Data Updated Successfully....'})
        else:
            return Response({'Error':'Data not Updated...'})
        

    def patch(self,request,id):
        PO=Product.objects.get(Product_id=id)
        JDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if JDO.is_valid():
            JDO.save()
            return Response({'value':'Data Updated Successfully....'})
        else:
            return Response({'Error':'Data not Updated...'})
    

    def delete(self,request,id):
        Product.objects.get(Product_id=id).delete()
        return Response({'value':'Data Deleted Successfully....'})
    
