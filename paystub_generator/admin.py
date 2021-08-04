from django.contrib import admin

# Register your models here.
from paystub_generator.models import State, Once, Daily, Weekly, Bi_Weekly, Semi_monthly, Monthly, Quartely, \
    Semi_annually, Annually, image_upld

admin.site.register(State)
admin.site.register(image_upld)
# admin.site.register(Daily)
# admin.site.register(Weekly)
# admin.site.register(Bi_Weekly)
# admin.site.register(Semi_monthly)
# admin.site.register(Monthly)
# admin.site.register(Quartely)
# admin.site.register(Semi_annually)
# admin.site.register(Annually)

