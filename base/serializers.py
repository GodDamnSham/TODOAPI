from rest_framework import serializers
from base.models import Task

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('user','id','aufgabe','Beschreibung','category','date','complete')