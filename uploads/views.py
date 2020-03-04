from django.shortcuts import render, redirect

from uploads.models import DocumentOne, DocumentTwo
from uploads.forms import DocumentOneForm, DocumentTwoForm


def home(request):
    documents_one = DocumentOne.objects.all()
    documents_two = DocumentTwo.objects.all()
    return render(request, 'home.html', {'documents_one': documents_one, 'documents_two': documents_two})


def form_one_upload(request):
    if request.method == 'POST':
        form = DocumentOneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentOneForm()
    return render(request, 'document_one_upload.html', {'form': form})


def form_two_upload(request):
    if request.method == 'POST':
        form = DocumentOneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentOneForm()
    return render(request, 'document_two_upload.html', {'form': form})
