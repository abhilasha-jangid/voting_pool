from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^pool/',include('pool.urls')),
    url(r'^accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="pool/login.html"), name="login"),
    url(r'^$',include('pool.urls'))
]
