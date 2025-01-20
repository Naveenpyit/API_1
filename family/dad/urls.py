from .views import capi_view,api_view,main_page
from django.urls import path

urlpatterns=[
    path('',main_page,name='mainview'),
    path('api/students/',capi_view,name='get&post'),
    path('api/students/<int:id>/',capi_view,name='put&del'),
    path('api/courses/',api_view,name='get&post'),
    path('api/courses/<int:id>',api_view,name='put&del'),
]