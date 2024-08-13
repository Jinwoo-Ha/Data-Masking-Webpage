# upload/views.py

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        file_url = fs.url(filename)
        return redirect('upload_success', file_url=file_url)
    return render(request, 'upload.html')

def upload_success(request, file_url):
    return render(request, 'success.html', {'file_url': file_url})


#추가
def upload_file(request):
    return render(request, 'upload.html')

def upload_success(request):
    return render(request, 'success.html')


def upload_file(request):
    return render(request, 'upload.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return render(request, 'api.html')

def contact_us(request):
    return render(request, 'contactus.html')
