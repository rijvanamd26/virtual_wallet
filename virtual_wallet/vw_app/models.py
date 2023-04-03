from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    balance = models.FloatField()

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sender',on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver',on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender_charges = models.FloatField(default=0.00)
    receiver_charges = models.FloatField(default=0.00)
    sender_wallet = models.FloatField(default=0.00)
    receiver_wallet = models.FloatField(default=0.00)

status_choice = {
    ('Accepted','Accepted'),
    ('Pending','Pending'),
    ('Denied','Denied'),
    ('Completed','Completed'),
}
class Request(models.Model):
    req_by = models.ForeignKey(User, related_name='req_by', on_delete=models.CASCADE)
    req_to = models.ForeignKey(User, related_name='req_to', on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=10,choices=status_choice,default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    