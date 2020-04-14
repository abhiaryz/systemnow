from django.contrib import admin
from .models import User, Server, Website
# Register your models here.

admin.site.register(User)
admin.site.register(Server)
admin.site.register(Website)