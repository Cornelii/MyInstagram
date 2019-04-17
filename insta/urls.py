from django.contrib import admin
from django.urls import path, include

#upload setting
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from posts import views as posts_views

urlpatterns = [
    path('', posts_views.list, name='root'),
    path('admin/asdf/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('<str:username>', accounts_views.people, name="people"),
    
]


# Dev only
# static(통과하고자 하는 url, 실제 저장 장소)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


