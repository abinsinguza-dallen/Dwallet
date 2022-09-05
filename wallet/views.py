from django.shortcuts import render
from .forms import CustomerRegestrationForm,CurrencyRegestrationForm,WalletRegestrationForm
from .forms import AccountRegestrationForm,TransactionRegestrationForm,CardRegestrationForm,ThirdpartyRegestrationForm,NotificationRegestrationForm
from.forms import LoanRegestrationForm,RecieptRegestrationForm,RewardRegestrationForm
# Create your views here.
def regester_customer(request):
    form=CustomerRegestrationForm()
    return render(request,"wallet/regester_customer.html",
{"form": form})

def currency(request):
    form=CurrencyRegestrationForm()
    return render(request,"wallet/currency.html",
{"form": form})
    
def wallet (request):
    form=WalletRegestrationForm()
    return render(request,"wallet/wallet.html",
{"form": form})   
    
def account (request):
    form=AccountRegestrationForm()
    return render(request,"wallet/account.html",
{"form": form})      
    
def transaction (request):
    form=TransactionRegestrationForm()
    return render(request,"wallet/transaction.html",
{"form": form})         
    
def card (request):
    form=CardRegestrationForm()
    return render(request,"wallet/card.html",
{"form": form})         
    
def thirdparty (request):
    form=ThirdpartyRegestrationForm()
    return render(request,"wallet/thirdparty.html",
{"form": form})       
    
def notification (request):
    form=NotificationRegestrationForm()
    return render(request,"wallet/notification.html",
{"form": form})        
    
def loan (request):
    form=LoanRegestrationForm()
    return render(request,"wallet/loan.html",
{"form": form})        
    
def reciept (request):
    form=RecieptRegestrationForm()
    return render(request,"wallet/reciept.html",
{"form": form})   
    
def reward (request):
    form=RewardRegestrationForm()
    return render(request,"wallet/reward.html",
{"form": form})           
    
       