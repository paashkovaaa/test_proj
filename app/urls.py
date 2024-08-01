from django.urls import path

from app.views import get_random_phrase, index

urlpatterns = [
        path("", index, name="index"),
        path("api/random-phrase/", get_random_phrase, name="random-phrase"),
]

app_name = "app"
