from django.urls import path
from .views import *
urlpatterns = [
    path('send_money/',SendMoneyView.as_view(),name='send_money'),
    path('request_money/',RequestMoneyView.as_view(),name='request_money'),
    path('requests_received/',RequestsReceivedView.as_view(),name='requests_received'),
    path('wallet/',WalletView.as_view(),name='wallet'),
     path('accept_req/<int:id>',AcceptReqView.as_view(),name='accept_req'),
    path('accept_req_status/<int:id>',AcceptReqStatusView.as_view(),name='accept_req_status'),
    path('deny_req_status/<int:id>',DenyReqStatusView.as_view(),name='deny_req_status') ,
]
