from django import forms
from uploads.models import DocumentOne, DocumentTwo


class DocumentOneForm(forms.ModelForm):
    class Meta:
        model = DocumentOne
        fields = ('description', 'document',)


class DocumentTwoForm(forms.ModelForm):
    class Meta:
        model = DocumentTwo
        fields = ('description', 'document',)