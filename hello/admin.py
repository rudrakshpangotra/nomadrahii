from django.contrib import admin
from . models import users1,users1_customize,hotels,shimla_customization,transport,spiti_customization,kinnaur_customization,dalhousie_customization,dharamshala_customization,manali_customization,price_of_basic_plan
admin.site.register(hotels)
admin.site.register(transport)
admin.site.register(users1)
admin.site.register(shimla_customization)
admin.site.register(users1_customize)
admin.site.register(spiti_customization)
admin.site.register(manali_customization)
admin.site.register(kinnaur_customization)
admin.site.register(dharamshala_customization)
admin.site.register(dalhousie_customization)
admin.site.register(price_of_basic_plan)
# Register your models here.
