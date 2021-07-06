from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
import csv
from django.contrib import messages

# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def list_records(request):
	header = 'Records'
	form = StockSearchForm(request.POST or None)
	queryset = record.objects.all()
	context = {
	"header": header,
    "queryset": queryset,
	"form": form,
	}
	if request.method == 'POST':
		queryset = record.objects.filter(item_name__icontains=form['item_name'].value()
										)

		#This part here is to export to csv using the same search button
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="Data.csv"'
			writer = csv.writer(response)
			#change these according to the data we have in the database, these are the heading for the csv file 
			#find a better way to do this (no hardcoding)
			writer.writerow(['CATEGORY', 'ITEM NAME', 'Created By'])
			instance = queryset
			for stock in instance:
				writer.writerow([stock.category, stock.item_name, stock.created_by])
			return response
	

		context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}
	return render(request, "list_records.html",context)



def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
	context = {
		"form": form,
		"title": "Add Record",
	}
	return render(request, "add_items.html", context)




def update_items(request, pk):
	queryset = record.objects.get(id=pk)
	form = RecordUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = RecordUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Updated')
			return redirect('/list_records')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)


def delete_items(request, pk):
	queryset = record.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Successfully Deleted')
		return redirect('/list_records')
	return render(request, 'delete_items.html')


def stock_detail(request, pk):
	queryset = record.objects.get(id=pk)
	context = {
		"queryset": queryset,
	}
	return render(request, "detail.html", context)

def goals (request):
	return render(request, 'goals.html')

def people (request):
	return render(request, 'people.html')	

def projects (request):
	return render(request, 'projects.html')	

def institutions (request):
	return render(request, 'institutions.html')	

def about (request):
	return render(request, 'about.html')

def contact (request):
	return render(request, 'contact.html')

def pricing (request):
	return render(request, 'pricing.html')

def faq (request):
	return render(request, 'faq.html')
	
def bloghome (request):
	return render(request, 'blog-home.html')



	