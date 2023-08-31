from django import forms
from listings.models import Band
from listings.models import Listing


class ContactUsForm(forms.Form):
   name = forms.CharField(required=False) # le champ name facultatif
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


#class BandForm(forms.Form):
#   name = forms.CharField(max_length=100)
#    biography = forms.CharField(max_length=100)
#    year_formed = forms.IntegerField(min_value=1900, max_value=2023)
#    official_homepage = forms.URLField(required=False)
#ou
class BandForm(forms.ModelForm):
   class Meta:

        model = Band
        #fields = '__all__' #si on veut des champs spécifiques il faut indiquer leur noms
        exclude = ('active', 'official_homepage')  # ajoutez cette ligne


class ListingForm(forms.ModelForm):
     class Meta:

        model = Listing
        #fields = '__all__' #si on veut des champs spécifiques il faut indiquer leur noms
        exclude = ('sold',)
