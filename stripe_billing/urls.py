from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import items.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', items.views.list_items, name='items_list'),
    path('item/<int:pk>/', items.views.item_detail, name='item_detail'),
    path('buy/<int:pk>/', items.views.create_checkout_session, name='item_buy'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
