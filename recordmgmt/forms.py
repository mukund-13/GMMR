from django import forms
from .models import record


#Form to add records, make changes here to include additional items for each record
class StockCreateForm(forms.ModelForm):
  class Meta:
    model = record
    fields = ['category', 'item_name', 'created_by']
     
  #Makes it required for a field to be completed 
  def clean_category(self):
    category = self.cleaned_data.get('category')
    if not category:
      raise forms.ValidationError('This field is required')
    return category
      
  def clean_item_name(self):
    item_name = self.cleaned_data.get('item_name')
    if not item_name:
      raise forms.ValidationError('This field is required')
      
    for instance in record.objects.all():
      if instance.item_name == item_name:
        raise forms.ValidationError(item_name + 'already exists')
    return item_name

  def clean_created_by(self):
    created_by = self.cleaned_data.get('created_by')
    if not created_by:
      raise forms.ValidationError('This field is required')
    return created_by


class StockSearchForm(forms.ModelForm):
  export_to_CSV = forms.BooleanField(required=False)
  class Meta:
    model = record
    fields = ['item_name']

class RecordUpdateForm(forms.ModelForm):
	class Meta:
		model = record
		fields = ['category', 'item_name']