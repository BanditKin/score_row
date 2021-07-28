from django.conf.urls import url
from .views import Score
urlpatterns = [
    url(r'^$', Score.as_view())
]
