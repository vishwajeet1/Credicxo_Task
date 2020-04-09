from rest_framework import serializers
from .models import Branches, Banks


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ['name', 'id']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'
