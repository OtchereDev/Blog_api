from django.urls import path,include
from .views import (PostListView,PostRetrieveUpdateDeleteView,
                    CategoryCreateView,CategoryUpdateView)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.oliv.ly/terms/",
      contact=openapi.Contact(email="oliverotchere4@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name='blog_api'


urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('cat/',CategoryCreateView.as_view(),name='cat_create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('cat/<id>/',CategoryUpdateView.as_view(),name='cat_update'),
   

    path('<int:id>/',PostRetrieveUpdateDeleteView.as_view(),name='post_detail'),

]
