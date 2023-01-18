from django.contrib import admin
from .models import EmailSendingFact, EmailType


admin.site.register(EmailType)

class EmailSendingFactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmailSendingFact._meta.fields]
    list_filter = ['email', 'type']
    search_fields = ['email', 'type']
    
    class Meta:
        model = EmailSendingFact
        
admin.site.register(EmailSendingFact, EmailSendingFactAdmin)
