from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from .models import *
from accounts.models import *
from rest_framework.response import Response

class SendMoneyView(APIView):
    def post(self, request):
        serializer = MoneySerializer(data=request.data)
        if serializer.is_valid():
            receiver = User.objects.get(username=serializer.data.get('username'))
            sender = request.user
            amount = serializer.data.get('amount')
            amount=float(amount)
            profile = Profile.objects.get(user=sender)
            swallet = Wallet.objects.get(user=sender)
            if swallet.balance >=amount:
                #updating sender wallet
                if profile.user_type == 'Premium':
                    sMoney = amount*0.03
                    swallet.balance -= amount
                    swallet.balance -= sMoney
                    swallet.save()
                else:
                    sMoney = amount*0.05
                    swallet.balance -= amount
                    swallet.balance -= sMoney
                    swallet.save()
                
                #updating receiver wallet
                receiver = User.objects.get(username=receiver)
                profile = Profile.objects.get(user=receiver)
                rwallet = Wallet.objects.get(user=receiver)

                if profile.user_type == 'Premium':
                    rMoney = amount*0.01
                    rwallet.balance += amount
                    rwallet.balance -= rMoney
                    rwallet.save()
                else:
                    rMoney = amount*0.03
                    rwallet.balance += amount
                    rwallet.balance -= rMoney
                    rwallet.save()

                # updating super user wallet
                money=sMoney+rMoney
                super_user = User.objects.get(is_superuser=True)
                if Wallet.objects.filter(user=super_user).exists():
                    super_user_wallet = Wallet.objects.get(user=super_user)
                    super_user_wallet.balance += money
                else:
                    Wallet.objects.create(user=super_user,balance=money)

                # updating transaction table
                transaction = Transaction.objects.create(sender=sender,receiver=receiver,amount=amount,sender_charges=sMoney,receiver_charges=rMoney,sender_wallet=swallet.balance,receiver_wallet=rwallet.balance)
                transaction.save()

                return redirect('home')
            else:
                print("sender wallet balance is less than amount which he want to send")
                return redirect('send_money')
        return redirect('send_money')
            
    def get(self, request):
        return render(request,"amount/send_money.html")
    
class RequestMoneyView(APIView):
    def post(self, request):
        serializer = MoneySerializer(data=request.data)
        if serializer.is_valid():
            req_by = request.user
            req_to =  User.objects.get(username=serializer.data.get('username'))     
            amount = serializer.data.get('amount')
            req_money = Request(req_to=req_to,req_by=req_by,amount=amount)
            req_money.save()
            return redirect("home")
        return redirect('request_money')

    def get(self, request):
        return render(request,"amount/request_money.html")

class RequestsReceivedView(APIView):
    def get(self, request):
        requests = Request.objects.filter(req_to=request.user)
        serializer = RequestSerializer(requests,many=True)
        print(serializer.data)
        context = {
            'requests':serializer.data,
        }
        return render(request,"requests_received.html",context)

class WalletView(APIView):
    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        sent = Transaction.objects.filter(sender=request.user)
        received = Transaction.objects.filter(receiver=request.user)
        wallet_serializer = WalletSerializer(wallet)
        sent_serializer = TransactionSerializer(sent,many=True)
        received_serializer = TransactionSerializer(received,many=True)
        context = {
            'wallet':wallet_serializer.data,
            'sent':sent_serializer.data,
            'received':received_serializer.data,
        }
        return render(request,"wallet.html",context)
    
class AcceptReqView(APIView):
    def post(self, request, id):
        req = Request.objects.get(pk=id)
        req.status = 'Accepted'
        req.save()
        serializer = RequestSerializer(req)
        data = serializer.data
        context = {
            'data': data
        }

        return render(request, 'amount/send_req_money.html',context)


class AcceptReqStatusView(APIView):
    def post(self, request,id):
        serializer = MoneySerializer(data=request.data)
        if serializer.is_valid():
            receiver = User.objects.get(username=serializer.data.get('username'))
            sender = request.user
            amount = serializer.data.get('amount')
            amount=float(amount)
            profile = Profile.objects.get(user=sender)
            swallet = Wallet.objects.get(user=sender)
            if swallet.balance >=amount:
                #updating sender wallet
                if profile.user_type == 'Premium':
                    sMoney = amount*0.03
                    swallet.balance -= amount
                    swallet.balance -= sMoney
                    swallet.save()
                else:
                    sMoney = amount*0.05
                    swallet.balance -= amount
                    swallet.balance -= sMoney
                    swallet.save()
                
                #updating receiver wallet
                receiver = User.objects.get(username=receiver)
                profile = Profile.objects.get(user=receiver)
                rwallet = Wallet.objects.get(user=receiver)
                if profile.user_type == 'Premium':
                    rMoney = amount*0.01
                    rwallet.balance += amount
                    rwallet.balance -= rMoney
                    rwallet.save()
                else:
                    rMoney = amount*0.03
                    rwallet.balance += amount
                    rwallet.balance -= rMoney
                    rwallet.save()

                # updating super user wallet
                money=sMoney+rMoney
                super_user = User.objects.get(is_superuser=True)
                if Wallet.objects.filter(user=super_user).exists():
                    super_user_wallet = Wallet.objects.get(user=super_user)
                    super_user_wallet.balance += money
                else:
                    Wallet.objects.create(user=super_user,balance=money)

                # updating transaction table
                transaction = Transaction.objects.create(sender=sender,receiver=receiver,amount=amount,sender_charges=sMoney,receiver_charges=rMoney,sender_wallet=swallet.balance,receiver_wallet=rwallet.balance)
                transaction.save()
                req = Request.objects.get(pk=id)
                req.status = 'Completed'
                req.save()

                return redirect('home')
            else:
                print("sender wallet balance is less than amount which he want to send")
                return redirect('send_req_money')
        return redirect('send_req_money')

class DenyReqStatusView(APIView):
    def post(self, request,id):
        req = Request.objects.get(pk=id)
        req.status = 'Denied'
        req.save()
        return redirect('home')
    