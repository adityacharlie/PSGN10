from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='PSGN10 API')

urlpatterns = [
    path('api/', schema_view),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('player/', include('core.urls')),
    prefix_default_language=False,
)
