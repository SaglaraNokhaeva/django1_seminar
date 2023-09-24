# Домашнее задание
# � Создайте пару представлений в вашем первом приложении:
# главная и о себе.
# � Внутри каждого представления должна быть переменная
# html - многострочный текст с HTML вёрсткой и данными о
# вашем первом Django сайте и о вас.
# � *Сохраняйте в логи данные о посещении страниц


from django.shortcuts import render
import random
from django.http import HttpResponse
import logging

# Create your views here.

logger = logging.getLogger(__name__)




def index(request):

 logger.info('Main page started')
 html = """"
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Главная</title>
</head>
<body>
Информация о моём первом сайте на Django
</body>
</html>
 """

 return HttpResponse(html)


def about(request):
 logger.info('About page started')
 html = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Обо мне</title>
</head>
<body>
Информация обо мне
</body>
</html>"""
 return HttpResponse(html)


