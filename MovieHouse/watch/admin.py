from django.contrib import admin
from watch.models import Mwatchlist,Swatchlist,Account,Month,Freetrial,Annual,Freetriallist
# Register your models here.
admin.site.register(Mwatchlist)
admin.site.register(Swatchlist)
admin.site.register(Account)
admin.site.register(Month)
admin.site.register(Freetrial)
admin.site.register(Annual)
admin.site.register(Freetriallist)