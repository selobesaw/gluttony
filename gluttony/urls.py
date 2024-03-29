"""gluttony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from gluttony.api_views import DishListCreateAPIView
from gluttony.views import DishLishView, OrderView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', DishLishView.as_view(), name='dish_list'),
    path('order/', OrderView.as_view(), name='order'),

    path('api/dishes/', DishListCreateAPIView.as_view(), name='api/dish_list_create'),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
