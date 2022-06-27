from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models  import SystemUser
from .serializers import systemUserSerializer
from django.core.files.storage import default_storage


@csrf_exempt
def systemuserApi(request, id=0):
    if request.method=='GET':
        systemuser = SystemUser.objects.all()
        systemuser_serializers= systemUserSerializer(systemuser, many=True)
        return JsonResponse(systemuser_serializers.data, safe=False)


    elif request.method=='POST':
        userdata = JSONParser().parse(request)
        systemuser_serializers = systemUserSerializer(data=userdata)
        if systemuser_serializers.is_valid():
            systemuser_serializers.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed To Added",safe=False)    

    elif request.method=='PUT':
        userdata = JSONParser().parse(request)
        users = SystemUser.objects.get(slugId=userdata['slugId'])
        systemuser_serializers = systemUserSerializer(users,data=userdata)
        if systemuser_serializers.is_valid():
            systemuser_serializers.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
