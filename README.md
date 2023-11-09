
# hw03_forms
### Сообщества создание записей

Добавлены следующие возможности:
- регистрация пользователя, 
- вход/выход пользователя,
- восстановления пароля,
- создания записей сообщества,
- подробная информация, редактирование только своей записи,
- отображение постов пользователя,
- пагинация, раздел Об авторе, Технологии, отображения профиля пользователя.

### Настройка и запуск

Клонируем проект:
```bash
git clone git@github.com:themasterid/hw03_forms.git
```

Переходим в папку с проектом:

```bash
cd hw03_forms
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
```
```bash
python yatube/manage.py migrate
```

Создаем superuser:

```bash
python yatube/manage.py createsuperuser
```

Собираем статику (опционально):

```bash
python yatube/manage.py collectstatic
```

Предварительно сняв комментарий с:
```bash
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

И закомментировав: 
```bash
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

Добавить в .gitingore файлы:

```bash
.env
.venv
```

Для запуска тестов выполним:

```bash
pytest
```



Запускаем проект:

```bash
python yatube/manage.py runserver
```

После чего проект будет доступен по адресу http://localhost:8000/

Заходим в http://localhost:8000/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Автор: [Daniil Petrov](https://github.com/octrow) :+1:
