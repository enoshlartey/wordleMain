from django import forms

class sixLetterWordForm(forms.Form):
    letterOne = forms.CharField(max_length=1, required=True, min_length=1)
    letterTwo = forms.CharField(max_length=1, required=True, min_length=1)
    letterThree = forms.CharField(max_length=1, required=True, min_length=1)
    letterFour = forms.CharField(max_length=1, required=True, min_length=1)
    letterFive = forms.CharField(max_length=1, required=True, min_length=1)
    letterSix = forms.CharField(max_length=1, required=True, min_length=1)