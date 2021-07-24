from django.urls import path
from .views import LinksView, AddLinksView

urlpatterns = [
    path('visited_domains/', LinksView.as_view(), name="visited_domains"),
    path('visited_links/', AddLinksView.as_view(), name="visited_links")
]