"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, PollUpdateView, PollCreateView, PollView, PollDeleteView, ChoiceForPollCreateView, \
    ChoiceUpdateView,ChoiceDeleteView,AnswerView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('poll/<int:pk>', PollView.as_view(),name='poll_view'),
    path('create/poll', PollCreateView.as_view(),name='poll_create'),
    path('update/poll/<int:pk>', PollUpdateView.as_view(),name='poll_update'),
    path('delete/poll/<int:pk>', PollDeleteView.as_view(),name='poll_delete'),
    path('create/choice/<int:pk>', ChoiceForPollCreateView.as_view(),name='poll_choice_create'),
    path('update/choice/<int:pk>', ChoiceUpdateView.as_view(),name='choice_update'),
    path('delete/choice/<int:pk>', ChoiceDeleteView.as_view(),name='choice_delete'),
    path('poll/<int:pk>/answer/',AnswerView.as_view(),name='answer')

]
