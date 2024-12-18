import os
import socket
import qrcode
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import UploadedFile

def generate_qr_code(file_url):
    qr = qrcode.make(file_url)
    qr_path = os.path.join(settings.MEDIA_ROOT, 'qr_codes', 'qr_code.png')

    os.makedirs(os.path.dirname(qr_path), exist_ok=True)

    qr.save(qr_path)
    return os.path.join(settings.MEDIA_URL, 'qr_codes/qr_code.png')


def upload_file(request):

    # Путь до директории для загруженных файлов и QR-кодов
    uploads_dir = os.path.join(settings.BASE_DIR, 'media', 'uploads')
    qr_codes_dir = os.path.join(settings.BASE_DIR, 'media', 'qr_codes')

    # Создаем директории, если их нет
    os.makedirs(uploads_dir, exist_ok=True)
    os.makedirs(qr_codes_dir, exist_ok=True)

    """Обработка загрузки файла и генерации QR-кода"""
    qr_code_url = None  # Изначально QR-код не сгенерирован
    form = FileUploadForm()  # Создаем форму, чтобы она была доступна и в случае GET, и в случае POST

    if request.method == 'POST':  # Если запрос POST (данные отправляются на сервер)
        form = FileUploadForm(request.POST, request.FILES)  # Переинициализируем форму с данными из POST и файлами из request.FILES
        if form.is_valid():  # Если форма валидна
            uploaded_file = form.save()  # Сохраняем загруженный файл в базу данных
            
            # Получаем локальный IP-адрес
            local_ip = socket.gethostbyname(socket.gethostname())
            
            # Формируем URL для скачивания файла
            file_url = f'http://{local_ip}:8000{settings.MEDIA_URL}{uploaded_file.file}'
            
            # Генерируем QR-код для этого URL
            qr_code_url = generate_qr_code(file_url)

    return render(request, 'file_uploader/upload.html', {
        'form': form,  # Передаем форму в шаблон
        'qr_code_url': qr_code_url,  # Передаем URL сгенерированного QR-кода в шаблон
    })