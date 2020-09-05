from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.routers import DefaultRouter
from realty.urls import router as realty_router

router = DefaultRouter()

router.extend(realty_router)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path("admin/", admin.site.urls),
    path('', include(router.urls)),

    path("", include("users.urls")),
    path("", include("reservation.urls")),
    path("", include("payment.urls")),
    path("", include("realty.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
