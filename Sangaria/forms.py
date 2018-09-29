from django import forms
from .models import Visitors,maintenance,Public
'''
class Visitors_form(forms.ModelForm):
	model=Visitors
	fields=["Name","checkin","checkout","purpose"]
'''


class Visitors_form_1(forms.Form):
	Name=forms.CharField(max_length=70)
	checkin=forms.IntegerField()
	checkout=forms.IntegerField()


class maintenance_modelform(forms.ModelForm):
	class Meta:

		model = maintenance
		fields="__all__"
	
class PublicModelform(forms.ModelForm):
	class Meta:
		model=Public
		fields=["name","contact"]
	






