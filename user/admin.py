from django.contrib import admin
from user.models import Contact,Menu

# Register your models here.
admin.site.site_header = 'YummyFoods | admin'
admin.site.register(Contact)
admin.site.register(Menu)
