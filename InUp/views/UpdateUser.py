from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from InUp.serializer import UserSerializer

@api_view(['PUT',])
@permission_classes((permissions.IsAdminUser,))

def UpdateUserApiview(request,pk):

    try:
        std=User.objects.get(pk=pk)
    except User.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='PUT':
        serializer=UserSerializer(std,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="data updated sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)