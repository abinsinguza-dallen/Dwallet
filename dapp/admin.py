from django.contrib import admin

# Register your models here.
from .models import Currency, Customer,Wallet,Account,Card,Thirdparty,Notification,Receipt,Loan,Reward,Transaction
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name","address")
    searchFields=("fist_name","last_name","address")
admin.site.register(Customer,CustomerAdmin) 

class WalletAdmin(admin.ModelAdmin):
    list_display=("customer","date_created")
    searchFields=("fist_name","last_name","address")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_number","account_type","wallet")
    searchFields=("account_name","account_number","account_type","wallet")
admin.site.register(Account,AccountAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("card_number"," card_type"," expiry_date","date_of_issue","cardStatus"," wallet","account","issuer")
    searchField=("card_number"," card_type"," expiry_date","date_of_issue","cardStatus"," wallet","account","issuer")
admin.site.register(Card)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("account","date_of_issue","wallet","issuer")
    searchFields=("account","date_of_issue","wallet","issuer")
admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("message","date","recipient","title")
    searchFields=("message","date","recipient","title")
admin.site.register(Notification,NotificationAdmin)

class RecipientAdmin(admin.ModelAdmin):
    list_display=("receipt_type","date","receipt_number","receipt_file")
    searchFields=("receipt_type","date","receipt_number","receipt_file")
admin.site.register(Receipt,RecipientAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_id","loan_type","amount","guaranter","issuer","wallet")
    searchFields=("loan_id","loan_type","amount","guaranter","issuer","wallet")
admin.site.register(Loan,LoanAdmin)

class ReawrdAdmin(admin.ModelAdmin):
    list_display=("recipient","date_of_reward","points")
    searchFields=("recipient","date_of_reward","points")
admin.site.register(Reward,ReawrdAdmin)

    

admin.site.register(Transaction)
admin.site.register(Currency)