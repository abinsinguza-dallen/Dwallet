from django.shortcuts import redirect, render

from wallet.models import Account, Currency, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction
from .forms import CustomerRegestrationForm,CurrencyRegestrationForm,WalletRegestrationForm
from .forms import AccountRegestrationForm,TransactionRegestrationForm,CardRegestrationForm,ThirdpartyRegestrationForm,NotificationRegestrationForm
from.forms import LoanRegestrationForm,RecieptRegestrationForm,RewardRegestrationForm,CustomerRegestrationForm
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
    
def register_Customer(request):
    if request.method=="POST":
        form=CustomerRegestrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CurrencyRegestrationForm()
    return render(request,"-----",{"form":form})     


def list_Customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/Customers_list.html", {"Customers":customers})                   
    
def list_Currencies(request):
    currencies=Currency.objects.all()
    return render(request,"wallet/Currency_list.html", {"Currency":currencies})                   
           
def list_Wallets(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html", {"Wallet":wallets}) 
                  
def list_Accounts(request):
    wallets=Account.objects.all()
    return render(request,"wallet/Account_list.html", {"Wallet":wallets})  

def list_Transaction(request):
    transaction=Transaction.objects.all()
    return render(request,"wallet/Transaction_list.html", {"Wallet":transaction}) 

def list_Cards(request):
    card=Card.objects.all()
    return render(request,"wallet/Transaction_list.html", {"Wallet":card}) 

def list_Thirdparty(request):
    thirdparty=Thirdparty.objects.all()
    return render(request,"wallet/Thirdparty_list.html", {"Wallet":thirdparty})   

def list_Notification(request):
    notification=Notification.objects.all()
    return render(request,"wallet/notification_list.html", {"Wallet":notification}) 

def list_Recipient(request):
    reciept=Receipt.objects.all()
    return render(request,"wallet/Recipient_list.html", {"Wallet":reciept})     

def list_loan(request):
    loan=Loan.objects.all()
    return render(request,"wallet/Loan_list.html", {"Wallet":loan})  

def list_reward(request):
    reward=Reward.objects.all()
    return render(request,"wallet/Reward_list.html", {"Wallet":reward})                   
                                                                          
                                                         
def customer_profile(request,id) :
    customer=Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer} )    


def edit_profile(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegestrationForm(request.POST,instance=customer)
        
        if form. is_valid():
            form.save()
            
        return redirect("customer_profile", id=customer.id)
    else:
        form =CustomerRegestrationForm(instance=customer)
        return render(request,"wallet/edit_profile.html",{"form":form})
    

                                                                          
                                                         
                                                                            
                                                            
                                                            
                                                            
                                                             
                                                            
                                           