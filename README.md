# Backend сервис для веб- и мобильного приложений проекта PetSeeker

Веб-приложение разработано с помощью веб-фреймворка Django Rest Framework <br>
uWSGI - Сервер приложений<br>
Swagger UI - API схемы <br>
PostgreSQL - СУБД <br>
Redis - сервис кэширования <br>
Firebase Cloud Messaging - отправка, таргетинг уведомлений <br>

## Deploy для разработки
```
cd ./backend
docker build -t pet_seeker_backend .
docker run -d -p 8000:8000 pet-seeker-backend
```