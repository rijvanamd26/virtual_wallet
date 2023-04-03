from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class MoneySerializer(serializers.Serializer):
    username = serializers.CharField()
    amount = serializers.FloatField()

    def validate(self, data):
        username = data.get('username')
        amount = data.get('amount')
        
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('User does not exist.')
        
        if amount<=0:
            raise serializers.ValidationError('Amount must be greater than zero.')

        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    

class RequestSerializer(serializers.ModelSerializer):
    req_by = UserSerializer()
    req_to = UserSerializer()
    class Meta:
        model = Request
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'
    
   