from django.contrib import admin

from .models import User
# Register your models here.

#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'email')
	search_fields = ('username', 'email')
	list_filter = ('is_superuser',)
	ordering = ('username',)
	filter_horizontal = ('groups', 'user_permissions')
	#actions = []

	fieldsets = (
			('User', {'fields': ('username', 'password')}),
			('Personal Info', {'fields': ('first_name', 'last_name', 'email',)}),
			('Permissions', {'fields': ('is_active',)}),
		)