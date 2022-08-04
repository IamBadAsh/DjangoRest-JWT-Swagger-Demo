from django.http import HttpResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Books.models import Booktmodel


@api_view(['DELETE',])
@permission_classes((permissions.IsAdminUser,))

def DeleteBookApiview(request,pk):

    try:
        std=Booktmodel.objects.get(pk=pk)
    except Booktmodel.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='DELETE':
        opperation=std.delete()
        data={}
        if opperation:
            data["success"]="data Deleted sucessfully"
        else:
            data['failed']="Unable to delete"
        return Response(data=data)
