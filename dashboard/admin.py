from django.contrib import admin
from .models import Client,ReceivedCargoKenya,MsgFromChina,ReceivedCargoChina, Remark,Subject,SalesAgent,ImajiAgent,DispatchCargoKenya,DispatchCargoChina
# Register your models here.
admin.site.register(Client)
admin.site.register(SalesAgent)
admin.site.register(Remark)
admin.site.register(Subject)
admin.site.register(ImajiAgent)
admin.site.register(ReceivedCargoKenya)
admin.site.register(DispatchCargoKenya)
admin.site.register(DispatchCargoChina)
admin.site.register(ReceivedCargoChina)

class MsgFromChinaAdmin(admin.ModelAdmin):
    list_display  = ['client_name','goods']

admin.site.register(MsgFromChina,MsgFromChinaAdmin)
