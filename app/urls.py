from django.urls import path
from .views import (LoginView,LogoutView,RegisterView,SendFriendRequestView,
                    FriendListView,AccpectRejectView,SearchUserView)

urlpatterns = [
    path('register/', RegisterView.as_view(),name='Register'),
    path('login/', LoginView.as_view(),name='Login'),
    path('logout/', LogoutView.as_view(),name='Logout'),
    path('send_friend_request/',SendFriendRequestView.as_view(),name='send-request'),
    path('get_freinds_list/',FriendListView.as_view(),name='friend-list'),
    path('accpect_reject_request/',AccpectRejectView.as_view(),name='accpect-reject'),
    path('search_user/',SearchUserView.as_view(),name='serach-user')
]