# Django QR Code File Sharing Project

## Описание
Это приложение позволяет загружать файл c пк, получать QR-код и скачивать файл на другое устройство, наведя на QR-код камерой телефона.

## Установка
1. Клонируйте репозиторий: git clone https://github.com/murzino/qr_file_exchange
2. Перейдите в папку проекта: cd qr_file_exchange
3. Установите зависимости: pip install -r requirements.txt
4. Выполните установку миграций БД: python manage.py migrate
5. Запустите сервер: python manage.py runserver 0.0.0.0:8000
6. Перейдите по адресу http://127.0.0.1:8000/

## Требования:
1. Для передачи файлов, устройства должны находиться в одной сети
