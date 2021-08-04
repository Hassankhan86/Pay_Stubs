from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from paystub import settings
from paystub_generator import views as paystub_gen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paystub_gen.homepage),

    path('w2_form/', include('W2_form.urls')),
    path('paystub_generator/', include('paystub_generator.urls')),
    path('misc_form_1099/', include('misc_form_1099.urls')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
