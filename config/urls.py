from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('blog/api/', include(('blog.urls', 'blog'), namespace='blog')),
    path('employee/api/', include(('employe.urls', 'employe'), namespace='employe')),
    path('portfolio/api/', include(('portfolio.urls', 'portfolio'), namespace='portfolio'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)