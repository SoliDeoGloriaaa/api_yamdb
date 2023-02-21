# Авторы
Над проектом работали Александр, Данил и Дмитрий, студенты Backend факультета Яндекс.Практикум.
На реализацию проекта потребовалось 9 дней!
# Технологии и их версии:
В проекте использовались такие технологии, как:
- requests==2.26.0
- Django==3.2
- djangorestframework==3.12.4
- PyJWT==2.1.0
- pytest==6.2.4
- pytest-django==4.4.0
- pytest-pythonpath==0.7.3
- djangorestframework-simplejwt==4.7.2
- django-filter~=22.1


# Описание проекта:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).


## Как запустить проект пользователям системы Windows: 
1. Клонировать репозиторий командой:
```
git clone <ссылка на репозиторий>.
```

2. Создать и активировать виртуальное окружении в корневой директории проекта:
 ```
python -m venv venv
```     
```
source venv/bin/activate
``` 

3. Установить зависимости командой:
```
pip install -r requirements.txt
```

4. Выполните миграции командой:
```
python manage.py migrate
```

5. Выполните команду для запуска dev-сервера
```
python manage.py runserver
```
