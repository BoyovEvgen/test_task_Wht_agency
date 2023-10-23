from django.contrib import admin


from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(Member, MemberAdmin)
