from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('home.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'home.views.page_404'
