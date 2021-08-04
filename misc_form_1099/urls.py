from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'misc_form'

urlpatterns = [

    path('misc_form_1099', views.misc_form_1099, name='misc_form_1099'),
    # path('create_your_stub',views.create_your_stub, name='create_your_stub'),

]
