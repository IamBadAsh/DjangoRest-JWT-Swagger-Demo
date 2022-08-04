from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Books.ApiSerializer import Serializer


@csrf_exempt
@api_view(['POST',])
@permission_classes((permissions.IsAdminUser ,))

def AddBookApiview(request):

    if request.method=='POST':
        serializer=Serializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="data Saved sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
