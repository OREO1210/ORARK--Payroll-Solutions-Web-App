"""orark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from accounts.views import view_logout
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hod/', include('hodapp.urls',namespace='hodapp')),
    path('emp/', include('empapp.urls',namespace='empapp')),
    path('logout/', view_logout),
    path('', include('accounts.urls')),
    path('leave/', include('leavemangement.urls',namespace='leavemangement')),
    path('recep/', include('attendence.urls',namespace='attendence')),
    path('ad/', include('salarymanagement.urls', namespace='salarymanagement')), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = "accounts.views.handle404"
handler500 = "accounts.views.handle500"
handler403 = "accounts.views.handle403"
handler400 = "accounts.views.handle400"
