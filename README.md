# VD04_web_Flask
## ___Flask_первое_знакомство___

Ну, что же, будем знакомиться...

### Задание 1 - branch task_1

Создаем новое приложение Flask, которое будет отображать текущие дату и время
на главной странице.

Реализуем задачу в ветке task_1

Два варианта решения:<br>

1 - вариант в файле main.py<br>

2- вариант в файле app.py со структурой flask т.е. задействованы файлы static/css/style и templates/index.html


### Задание 2 - branch main

Создаем новое приложение Flask. <br>Формируем правильную структуру проекта с папками<br>
static и templates, в папке templates размещаем html файлы:<br> index, blog,
contacts, base, about_them <br>(главная страница, страница блога, контакты,
контейнер меню, аккордеон с информацией об актерах).<br> в папке static папка css с файлом style.css<br>
Заполняем их информацией и выводим силами flask сервера,
используя функцию render_template()

Делаем меню на всех страницах, оно должно будет работать именно при
запуске проекта через flask
Слайдер работает и без него, на html.