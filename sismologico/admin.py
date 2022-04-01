from django.contrib import admin
from .models import User, Sismo, Article
# Register your models here.
admin.site.register(User)
admin.site.register(Sismo)
admin.site.register(Article)