"""
URL configuration for health project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import homepage
from accounts.views import register, login, logout
from therapists.views import dashboard, schedule_view, schedule_create, schedule_delete, schedule_show, schedule_update
from patient.views import index, clinic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('therapist/dashboard/', dashboard, name='dashboard' ),
    path('therapist/schedule', schedule_view, name='schedule'),
    path('therapist/show/<int:schedule_id>/', schedule_show, name='schedule.show'),
    path('therapist/create/', schedule_create, name='schedule.create'),
    path('therapist/update/<int:schedule_id>/', schedule_update, name='schedule.update'),
    path('therapist/delete/<int:schedule_id>/', schedule_delete, name='schedule.delete'),
    path('test/', index, name='test'),
    path('results/', clinic, name='results'),
]
