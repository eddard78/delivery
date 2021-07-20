from django.contrib import admin
from django.urls import path, include

from users.views import ProfileRegisterView, ProfileLoginView, StuffRegisterView, StuffLoginView, CourierRegisterView, CourierLoginView
from categories.views import CategoriesView

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="MIO DELEVER API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/register', ProfileRegisterView.as_view()),
    path('profile/login', ProfileLoginView.as_view()),
    path('stuff/register', StuffRegisterView.as_view()),
    path('stuff/login', StuffLoginView.as_view()),    
    path('courier/register', CourierRegisterView.as_view()),
    path('courier/login', CourierLoginView.as_view()),
    path('orders/', include('orders.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)