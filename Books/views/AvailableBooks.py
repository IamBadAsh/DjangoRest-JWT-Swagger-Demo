from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Books.ApiSerializer import Serializer
from Books.models import Booktmodel


@api_view(['GET',])
@permission_classes((permissions.IsAuthenticated,))
def AvailableBooksApiview(request):

    try:
        std=Booktmodel.objects.all().filter(status="AVAILABLE")
    except Booktmodel.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='GET':
        serializer=Serializer(std,many=True)
        return Response(serializer.data)
