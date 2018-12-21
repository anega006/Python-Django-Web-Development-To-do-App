from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()  #Saving to database
			messages.success(request, 'Item has been added successfully to the to-do list!')
		all_list_items = List.objects.all()
		context = {'all_list_items': all_list_items}
		return render(request, 'todo_app/index.html', context)
	else:
		all_list_items = List.objects.all()
		context = {'all_list_items': all_list_items}
		return render(request, 'todo_app/index.html', context)


def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.warning(request, 'Item has been deleted from the to-do list!')
	return redirect('index')


def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)
		if form.is_valid():
			form.save()  #Saving to database
			messages.success(request, 'Item has been edited successfully!')
		return redirect('index')
	else:
		item = List.objects.get(pk=list_id)
		context = {'item': item}
		return render(request, 'todo_app/edit.html', context)


def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('index')


def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('index')