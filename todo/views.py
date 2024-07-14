from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.urls import reverse, reverse_lazy

from .models import*
# Create your views here.

class HomePageView(ListView):
    model = ToDoList
    template_name = 'todo/index.html'

class ItemListView(ListView):
    model = TodoItem
    template_name = 'todo/todo_list.html'

    def get_query_set(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

    def get_context_data(self):
        context = super().get_context_data()
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['object_list'] = TodoItem.objects.filter(todo_list=context['todo_list'])
        return context

class ListCreateView(CreateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todo/todolist_form.html'

    def get_context_data(self):
        context = super(ListCreateView, self).get_context_data()
        context['title'] = 'Add a new list'
        return context

class ItemTaskCreateView(CreateView):
    model = TodoItem
    template_name = 'todo/item_form.html'
    fields = ['todo_list', 'title', 'description', 'due_date']

    def get_initial(self):
        initial_data = super(ItemTaskCreateView, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemTaskCreateView, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context

    def get_success_url(self):
        return reverse('todo-list', args=[self.object.todo_list_id])

class ItemUpdateTaskView(UpdateView):
    model = TodoItem
    fields = ['todo_list', 'title', 'description', 'due_date']
    template_name = 'todo/item_form.html'

    def get_context_data(self):
        context = super(ItemUpdateTaskView, self).get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context

    def get_success_url(self):
        return reverse('todo-list', args=[self.object.todo_list_id])


class ListDeleteView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('index')

class TaskDeleteView(DeleteView):
    model = TodoItem

    def get_success_url(self):
        return reverse_lazy('todo-list', args=[self.kwargs['list_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = self.object.todo_list
        return context