# Задание №5
# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
# � Пропишите маршруты

from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.


def one(request):
 answer = ['Орел', 'Решка']
 i = random.randint(0, 1)
 return HttpResponse(f"{answer[i]}")

def two(request):
 answer = random.randint(1, 6)
 return HttpResponse(f"{answer}")

def three(request):
 answer = random.randint(0, 100)
 return HttpResponse(f"{answer}")