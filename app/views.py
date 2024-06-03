from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,FriendRequestSerializer,FriendListSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.validators import ValidationError
from .models import FriendRequest,FriendList
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import generics
from rest_framework import filters
from .pagination import SerachUserPagination
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        userserializer = UserSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            result = {
                "data":userserializer.data,
                "message":"successful"
            }
            return Response(result,status=status.HTTP_201_CREATED)
        else:
            return Response(userserializer.errors)

class LoginView(APIView):
    def post(self,request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        if user:
            token,cretaed = Token.objects.get_or_create(user=user)
            value = {"token":token.key,
                     "message":"successful"}
            return Response(value,status=status.HTTP_200_OK)
        else:
            raise ValidationError({"error":"User Not Found"})

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"data":"logged out successfully",
                         "message":"successful"})

class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'send-request'
    def post(self,request):
        friendreqserializer = FriendRequestSerializer(data=request.data)
        if friendreqserializer.is_valid():
            friendreqserializer.save()
            temp = {
                "data":"Friend Request Sent successfully",
                "message":"successful"
            }
            return Response(temp,status=status.HTTP_201_CREATED)
        else:
            return Response(friendreqserializer.errors)

class FriendListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        id = request.user.id
        user = get_object_or_404(User,id=id)
        friends_list = FriendList.objects.filter(user = user)
        serializer = FriendListSerializer(friends_list,many=True)
        values= serializer.data
        result = []
        for value in values:
            temp = {
                "user": str(user),
                "friends" : [str(get_object_or_404(User,id=x)) for x in value['friends']]
            }
            result.append(temp)
        return Response(result,status=status.HTTP_200_OK)

class AccpectRejectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user.id
        requests = FriendRequest.objects.filter(receiver=user,is_active=False).values()
        # print(User.objects.get(pk=user))
        result = []
        for i in requests:
            temp = {
                "id":i['id'],
                "sender": str(User.objects.get(pk=i['sender_id'])),
                "receiver" : str(User.objects.get(pk=i['receiver_id'])),
                "status": i['is_active'],
                "sent time":i['created_at']

            }
            result.append(temp)
        return Response(result,status=status.HTTP_200_OK)

    def put(self,request):
        pk = request.data['pk']
        req_status = request.data['status']
        value = False
        if req_status == 'YES':
            value = True
        if value:
            rec_id = request.user.id
            f_request = FriendRequest.objects.get(pk=pk)
            f_request.is_active = value
            f_request.save()
            sender_user = FriendRequest.objects.filter(pk=pk).values()
            send_id = sender_user[0]['sender_id']
            sender = get_object_or_404(User,id =send_id)
            reciver = get_object_or_404(User,id=rec_id)
            test = FriendList.objects.get(user=reciver)
            test.friends.add(sender.id)
            result = {"data":"Friend request accpected"}
            return Response(result,status=status.HTTP_200_OK)
        else:
            result = {"data": "Friend request Rejected"}
            return Response(result)

class SearchUserView(generics.ListAPIView):
    pagination_class = SerachUserPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    queryset = User.objects.all()
    serializer_class = UserSerializer




