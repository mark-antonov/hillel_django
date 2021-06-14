<h1> Hometasks for Hillel. </h1>

<strong>Hometask 5. queryset filter, management commands:</strong><br>

Написать кастомную менеджент комманду которая будет генеритовать случайных пользователей ( https://docs.djangoproject.com/en/3.1/ref/models/querysets/#create ) c username, email и password. Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. Значения меньше 1 и больше 10 - должны вызывать ошибку.
https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/ <br>
Run the following command.
```
python manage.py create_users <number_of_users>
```

<strong>Hometask 6. Django forms:</strong><br>

Добавить вью по пути `/triangle`<br>
На этой вью необходимо использовать форму которая будет принимать значения двух катетов треугольника (положительные, больше нуля, для простоты используйте int значения если хотите). После отправки формы, если значения были валидными - на этой же странице вывести значение гипотенузы.<br>
Это должна быть одна view. <br>
Можете использовать 1 или 2 темплейта при необходимости для рендера формы и результата.
Если один темплейт - значение гипотенузы по умолчанию None - проверяйте его в темплейте, и на основании того None или "значение" рендерите форму или значение гипотенузы.

<strong>Homework 7. Django model form:</strong><br>

Создать новую модель с несколькими полями. Создать миграцию и мигрировать.<br>

Person:<br>
- first_name - CharField<br>
- last_name - CharField<br>
- email - EmailField<br>

Создать modelform, view, template - для создания новой записи, и для редактирования существующей записи.<br>
<br>
URLS:<br>
- `/person - GET` - получить форму<br>
- `/person - POST` - отвалидировать и сохранить новый объект Person в базу<br>
- `/person/<id:int> - GET` - получить форму с данными Person, или 404 если пользователя с таким id не существует<br>
- `/person/<id:int> - POST` - обновить данные Person, или 404


<strong>HT 8. OneToOneField, ForeignKey, ManyToManyField: </strong><br>
Реализовать в приложении модели использующие поля OneToOneField, ForeignKey, ManyToManyField.

Использовать graph_models из django-extensions что бы отобразить структуру моделей ТОЛЬКО этого приложения.

Пример:

- Город
- Клиент (MTM на товар, FK на город)
- Товар
- Поставщик (OTO на город)

Написать по запросу из инстанса одной модели в другую по каждой из связей (всего 3 запроса).

Для создания запроса используйте `shell_plus --print-sql` что бы ваш SQL отобразился в консоли.


<strong>Hometask 9. Middleware for logging requests, ModelAdmin:</strong><br>
Добавить модель для логов. В ней должны быть поля - path (путь), method (GET, POST etc), timestamp.
Добавить мидлвар LogMiddleware который будет обрабатывать каждый реквест (кроме реквестов в админку) и сохранять соответствующие значения в базу.<br>
Добавить ModelAdmin для этой модели что бы вывести соответствующие данные в админке.