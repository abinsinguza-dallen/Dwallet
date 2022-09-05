
from django import forms
from .models import Currency,Customer,Reward, Notification, Receipt, Thirdparty, Transaction,Wallet,Account,Transaction,Card,Thirdparty,Loan

class CustomerRegestrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        
class CurrencyRegestrationForm(forms.ModelForm):
    class Meta:
        model=Currency
        fields="__all__"        
        
class WalletRegestrationForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"    
        
class AccountRegestrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"       
        
class TransactionRegestrationForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"  
          
class CardRegestrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields="__all__"                              
                    
class ThirdpartyRegestrationForm(forms.ModelForm):
    class Meta:
        model=Thirdparty
        fields="__all__"                              
                                        
class NotificationRegestrationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields="__all__"              
        
class LoanRegestrationForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields="__all__"      
        
class RecieptRegestrationForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields="__all__"                             
        
class RewardRegestrationForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields="__all__"            