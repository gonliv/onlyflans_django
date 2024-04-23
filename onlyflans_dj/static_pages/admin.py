from django.contrib import admin
from .models import Flan
from .models import ContactForm


# Register your models here.

admin.site.register(Flan)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'message')
    search_fields = ('customer_name', 'customer_email')
    readonly_fields = ('contact_form_uuid',)