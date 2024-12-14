from django.contrib import admin
from person.models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = (
        Profile.image.field.name,
        Profile.birthday.field.name,
    )
