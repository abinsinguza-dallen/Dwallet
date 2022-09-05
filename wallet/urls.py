from django.urls import path

from wallet.models import Notification
from .views import currency, regester_customer, reward,transaction,wallet,account,card,thirdparty,notification,loan,reciept


urlpatterns = [
    path ("regester/",regester_customer, name="regestration"),  
    path ("currency/",currency, name="regestration"),  
    path ("wallet/",wallet, name="regestration"),  
    path ("account/",account, name="regestration"),  
    path ("transaction/",transaction, name="regestration"), 
    path ("card/",card, name="regestration"),  
    path ("thirdparty/",thirdparty, name="regestration"),  
    path ("notification/",notification, name="regestration"),  
    path ("loan/",loan, name="regestration"),  
    path ("reciept/",reciept, name="regestration"),  
    path ("reward/",reward, name="regestration"),  





 



]