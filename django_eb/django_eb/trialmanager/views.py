from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

import json

from django.http import HttpResponse

from django_eb.trialmanager.models import Profile
from django_eb.trialmanager.serializers import ProfileSerializer

from django_eb.trialmanager.models import Greeting
from django_eb.trialmanager.serializers import GreetingSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the trialmanager index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


@api_view(['GET', 'POST'])
def profile_list(request):
    """
    List all profiles, or create a new profile.
    """
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def greeting_list(request):
    """
    List all greetings, or create a new greeting.
    """

    parser_classes = (JSONParser,)

    if request.method == 'GET':
        greetings = Greeting.objects.all()
        serializer = GreetingSerializer(greetings, many=True)

        for obj in serializer.data:
        	parsed_data = json.loads(obj['data'])
        	obj['data'] = parsed_data

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



