from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from .models import FriendList,FriendRequest



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password',)
        extra_kwargs = {
            "password":{'write_only':True}
        }

    def save(self):

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise ValidationError({'error': 'Email already exists!'})
        password = self.validated_data['password']

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        frilend_list = FriendList.objects.create(user=account)
        return account


class FriendListSerializer(ModelSerializer):
    class Meta:
        model = FriendList
        fields = '__all__'


class FriendRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'