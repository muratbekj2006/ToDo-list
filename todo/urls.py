from django.urls import path

from .views import*
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo-list/<int:list_id>/', ItemListView.as_view(), name='todo-list'),
    path('todo-list/add', ListCreateView.as_view(), name='todo-list-add'),
    path('todo-list/<int:list_id>/item/add/', ItemTaskCreateView.as_view(), name='task-add'),
    path('todo-list/<int:list_id>/item/update/<int:pk>/', ItemUpdateTaskView.as_view(), name='item-update'),
    path('todo-list/<int:list_id>/delete', ListDeleteView.as_view(), name='list-delete'),
    path('todo-list/<int:list_id>/item/<int:pk>/delete', TaskDeleteView.as_view(), name='item-delete')
]