"""
URL configuration for study_REST project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpaPlease complete your account verification. We’ve sent the verification link to pip_install_gggrents@mail.rutterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasklist/<int:pk>', TaskAPIallfunc.as_view()),
    path('api/tasklist/', TaskApiupdView.as_view()),
    path('api/tasklist/lst', TaskApiupdViewLst.as_view()),
    path('api/tasklist/crt', TaskApiupdViewCrt.as_view()),
  #  path('api/v1/testapi/', TestApiView.as_view()),

]