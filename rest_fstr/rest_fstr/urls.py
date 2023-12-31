"""
URL configuration for rest_fstr project.

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
from rest.views import (
    SubmitDataView,
    UserView,
    CoordsView,
    PerevalImagesView,
    PerevalAreasView,
    SprActivitiesTypesView,
)
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="API documentation for the project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submit-data/', SubmitDataView.as_view(), name='submit-data'),
    path('api/submit-data/<int:id>/', SubmitDataView.as_view(), name='submit-data-detail'),
    path('api/user/', UserView.as_view(), name='user'),
    path('api/user/<int:id>/', UserView.as_view(), name='user-detail'),
    path('api/coords/', CoordsView.as_view(), name='coords'),
    path('api/coords/<int:id>/', CoordsView.as_view(), name='coords-detail'),
    path('api/pereval-images/', PerevalImagesView.as_view(), name='pereval-images'),
    path('api/pereval-images/<int:id>/', PerevalImagesView.as_view(), name='pereval-images-detail'),
    path('api/pereval-areas/', PerevalAreasView.as_view(), name='pereval-areas'),
    path('api/pereval-areas/<int:id>/', PerevalAreasView.as_view(), name='pereval-areas-detail'),
    path('api/spr-activities-types/', SprActivitiesTypesView.as_view(), name='spr-activities-types'),
    path('api/spr-activities-types/<int:id>/', SprActivitiesTypesView.as_view(), name='spr-activities-types-detail'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

