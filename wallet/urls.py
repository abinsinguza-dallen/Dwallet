from django.urls import path

from wallet.models import Notification
from .views import currency, customer_profile, edit_profile, list_Currencies, list_Customers, regester_customer, reward,transaction,wallet,account,card,thirdparty,notification,loan,reciept
from .views import list_Wallets,list_Thirdparty,list_Notification,list_Recipient,list_loan

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
    
    # Lists
    path("Customers/", list_Customers, name="customers_list"),
    path("Currencies/",list_Currencies, name="list_Currencies"),
    path("Wallets/",list_Wallets, name="list_Wallets"),
    path("Thirdpartys/",list_Thirdparty, name="list_Thirdparty"),
    path("Notifications/",list_Notification, name="list_Notification"),
    path("Recipients/",list_Recipient, name="list_Recipient"),
    path("Loans/",list_loan ,name="list_loan"),
    
    # single object view
path ("Customers/<int:id>/", customer_profile,name="customer_profile"),

path("Customers/edit/<int:id>/", edit_profile,name="edit_profile"),











 



]