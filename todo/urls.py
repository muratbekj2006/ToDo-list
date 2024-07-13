from django.urls import path

from .views import*
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo-list/<int:list_id>/', ItemListView.as_view(), name='todo-list'),
    path('todo-list/add', ListCreateView.as_view(), name='todo-list-add')
    path('todo-list/<int:list_id>/item/add/', ItemTaskCreateView.as_view(), name='task-add'),
    path('todo-list/<int:list_id>/item/update/', ItemUpdateTaskView.as_view(), name='item-update'),
]