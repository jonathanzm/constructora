from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import ugettext_lazy as _


from cliente.models import Cliente
from cliente.forms import ClienteChangeForm, ClienteCreationForm

from django.conf.urls import url

class UserAdmin(UserAdmin):
	def get_urls(self):
		return [
			url(r'^(.+)/password/$', self.admin_site.admin_view(self.user_change_password), name='auth_user_password_change'),
		] + super(UserAdmin, self).get_urls()

# @admin.register(Cliente)
class ClienteAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('cedula', 'first_name', 'last_name', 'titulaciones', 'seccion')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'cedula', 'password1', 'password2')}
		),
	)
	form = ClienteChangeForm
	add_form = ClienteCreationForm

	list_display = ('id','username', 'cedula', 'first_name', 'last_name')
	list_filter = ('is_superuser', 'is_active', 'groups', 'is_staff',)
	search_fields = ('username', 'email', 'first_name', 'last_name')
	ordering = ('username',)
	filter_horizontal = ('groups', 'user_permissions')

admin.site.register(Cliente, ClienteAdmin)

