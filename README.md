# 5 букв
Данное приложение представляет из себя веб-игру 5 букв, задачей которой является отгадать загаданное слово из 5 букв за 6 попыток. Приложение написано на языке Python на основе RESTfull на библиотеке Flask.

# Запуск
Приложение поставляется в Docker контейнера. Для развертывания необходимо выполнить следующую команду в директории приложения
```
docker-compose -f docker/docker-compose.yml up -d
```
Приложение развертывается локально по адресу 127.0.0.1:5000

# API
Для получения случайного слова из банка реализована возможность послать get-запрос. Пример запроса представлен в виде коллекции Postman: https://www.postman.com/avionics-geoscientist-66862444/workspace/wordly
