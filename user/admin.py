from django.contrib import admin
from user.models import Contact,Menu,Gallery,Chef

# Register your models here.
admin.site.site_header = 'YummyFoods | admin'
admin.site.register(Contact)
admin.site.register(Menu)
admin.site.register(Gallery)
admin.site.register(Chef)

