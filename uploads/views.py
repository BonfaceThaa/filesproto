from django.shortcuts import render, redirect

from uploads.forms import DocumentOneForm, DocumentTwoForm


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
