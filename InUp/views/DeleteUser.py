from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['DELETE',])
@permission_classes((permissions.IsAdminUser,))

def DeleteUserApiview(request,pk):

    try:
        std=User.objects.get(pk=pk)
    except User.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='DELETE':
        opperation=std.delete()
        data={}
        if opperation:
            data["success"]="data Deleted sucessfully"
        else:
            data['failed']="Unable to delete"
        return Response(data=data)
