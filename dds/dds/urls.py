"""
URL configuration for dds project.

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include('match.urls'), name="home"),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about') ,
    path('league/', include('league.urls')),
    path('season/', include('season.urls')),
    path('league_season/', include('league_season.urls')),
    path('location/', include('location.urls')),
    path('team/', include('team.urls')),
    path('role/', include('role.urls')),
    path('event_type/', include('event_type.urls')),
    path('event_roster/', include('event_roster.urls')),
    path('point/', include('point.urls')),    
    path('match/', include('match.urls')),
    path('match_type/', include('match_type.urls')),
    path('user_ref/', include('user_ref.urls')),
    path('user/', include('user.urls')),
    path('event/', include('event.urls')),
    path('timeout/', include('timeout.urls')),
    path('user_team/', include('user_team.urls')),
    path('rules/', include('rules.urls')),
    path('court/', include('court.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
