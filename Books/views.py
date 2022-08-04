from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .ApiSerializer import Serializer
from .models import Booktmodel

@csrf_exempt
@api_view(['POST',])
@permission_classes((permissions.IsAdminUser ,))

def book_Add_apiview(request):

    if request.method=='POST':
        serializer=Serializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="data Saved sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def student_getStudent_view(request):

    try:
        std=Booktmodel.objects.all().filter(status="AVAILABLE")
    except Booktmodel.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='GET':
        serializer=Serializer(std,many=True)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((permissions.IsAdminUser,))

def student_Update_one_apiview(request,pk):

    try:
        std=Booktmodel.objects.get(pk=pk)
    except Booktmodel.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='PUT':
        serializer=Serializer(std,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="data updated sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((permissions.IsAdminUser,))

def student_Delete_one_apiview(request,pk):

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


@api_view(['PUT',])
@permission_classes((permissions.AllowAny,))

def IssueBook_apiview(request,pk):

    try:
        std=Booktmodel.objects.get(pk=pk)
    except Booktmodel.DoesNotExist:
      return HttpResponse(status=404)

    if request.method=='PUT':
        data = {"status": "BORROWED"}
        serializer=Serializer(std,data=data,partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="data updated sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT',])
@permission_classes((permissions.AllowAny,))

def returnBook_apiview(request,pk):

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

