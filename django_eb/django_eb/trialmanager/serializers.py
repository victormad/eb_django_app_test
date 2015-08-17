from rest_framework import serializers

from .models import Profile
from .models import Greeting


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id','username','interaction')

class GreetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Greeting
        fields = ('id','name','data')