from django.urls import path
from . import views
from .views import TaskList

urlpatterns=[
    path('',views.tasklist,name='tasklist'),
    path('',TaskList.as_view(),name='tasks')
]