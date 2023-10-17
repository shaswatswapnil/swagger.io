# urls.py
from django.urls import path
from .views import GoogleSheetDataAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="googlespreed sheet API",
        default_version="v1",
        description="googlespreed sheet api",
        terms_of_service="https://www.yourterms.com/",
        contact=openapi.Contact(email="shaswat785@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/google-sheet-data/', GoogleSheetDataAPIView.as_view(), name='google-sheet-data'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]


