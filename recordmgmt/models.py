from django.db import models


#This is used to add the choice to a field
category_choice = (
	('DATA', 'DATA'),
	('IMG', 'IMG'),
)

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name

#This model is for record keeping, add new fields here to include additional fields
class record(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.item_name








