from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #do tego zeby nie dalo sie edytowac hasla wpanelu admina
from .models import Account

class AccountAdmin(UserAdmin): #do tego zeby nie dalo sie edytowac hasla wpanelu admina
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active' )#zeby wywietlalo sie przy emailu
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
