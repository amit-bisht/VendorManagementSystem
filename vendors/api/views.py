from rest_framework.response import Response
from rest_framework.decorators import api_view
from vendors.models import Vendor
from .serializers import VendorSerializer
@api_view(['GET','POST'])
def vendor_method(request):
    if(request.method=="GET"):
        vendors_list=Vendor.objects.all()
        serializer=VendorSerializer(vendors_list,many=True)
        return Response(serializer)
    elif(request.method=="POST"):
        pass
         