from django.urls import path

import tracker_ui.views

urlpatterns = [
    path('', tracker_ui.views.index),
]
