from django.urls import path, include
from .views import home, massageCreateView

app_name = 'chatroom'

urlpatterns = [
    path('', home, name='rootchat'),
    path("gh", massageCreateView.as_view(), name="gh")
]