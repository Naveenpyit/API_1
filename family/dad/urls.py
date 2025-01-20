from .views import capi_view,api_view
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('api/students/',capi_view,name='get&post'),
    path('api/students/<int:id>/',capi_view,name='put&del'),
    path('api/courses/',api_view,name='get&post'),
    path('api/courses/<int:id>',api_view,name='put&del'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]