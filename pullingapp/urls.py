"""pullingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.benchmark, name='benchmark')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='benchmark')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views as auth_views
import members.views as members_views
import benchmark.views as benchmark_views
import login.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^members/dashboard$', members_views.dashboard, name='dashboard'),
    url('register', include('register.urls')),
    url('login', include('login.urls')),
    url(r'^$', benchmark_views.homepage, name='homepage'),
    url(r'^members/benchmark$', benchmark_views.benchmark, name='benchmark'),
    url(r'^save_vote_data', benchmark_views.save_vote_data),
    url(r'^save_comment_data', benchmark_views.save_comment_data),
    url(r'^get_chart_data', benchmark_views.get_chart_data),
    url(r'^login$', login.views.login, name='login'),
    url(r'^logout$', auth_views.LogoutView.as_view(), name='logout')
]