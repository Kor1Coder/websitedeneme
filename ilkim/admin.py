from django.contrib import admin
from .models import Form,solide,siemene,matlabe,gamedevelope,guie,pythone,gamedevelopslavee
class formadmin(admin.ModelAdmin):
    list_display =['name','email','option']
    search_fields =['name','surname','email','option']
    list_filter =['name','email','option']

admin.site.register(Form,formadmin)

class solidadmin(admin.ModelAdmin):
    list_display =['title','goal','date']
    search_fields =['title','goal','date','begen']
    list_filter =['title','goal','date','begen']
admin.site.register(solide,solidadmin)
class siemenadmin(admin.ModelAdmin):
    list_display =['title','goal','date']
    search_fields =['title','goal','date','begen']
    list_filter =['title','goal','date','begen']
admin.site.register(siemene,siemenadmin)

admin.site.register(matlabe)
admin.site.register(gamedevelope)
admin.site.register(guie)
admin.site.register(pythone)
admin.site.register(gamedevelopslavee)