from django.contrib import admin
from django.urls import path, include

#upload setting
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]


# Dev only
# static(통과하고자 하는 url, 실제 저장 장소)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


