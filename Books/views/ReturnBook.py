from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Books.ApiSerializer import Serializer
from Books.models import Booktmodel


@api_view(['PUT',])
@permission_classes((permissions.IsAuthenticated,))

def ReturnBookApiview(request,pk):

    try:
        std=Booktmodel.objects.get(pk=pk)
    except Booktmodel.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='PUT':
        data = {"status": "AVAILABLE"}
        serializer=Serializer(std,data=data,partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="data updated sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

