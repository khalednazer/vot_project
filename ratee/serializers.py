from .models import ask
from rest_framework import serializers


class seruser(serializers.ModelSerializer):
    class Meta:
        model  = ask
        fields ='__all__'