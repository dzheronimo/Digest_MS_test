from django.urls import path
from .views import DigestView

urlpatterns = [
    path('digest/', DigestView.as_view(), name='digest')
]