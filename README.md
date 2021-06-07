<h1> Hometasks Hillel. </h1>

<strong>Hometask 5. queryset filter, management commands:</strong><br>

Написать кастомную менеджент комманду которая будет генеритовать случайных пользователей ( https://docs.djangoproject.com/en/3.1/ref/models/querysets/#create ) c username, email и password. Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. Значения меньше 1 и больше 10 - должны вызывать ошибку.
https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/ <br>
Run the following command.
```
python manage.py create_users <number_of_users>
```