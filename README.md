# Куда пойти в Москве

Интерактивная карта Москвы. Нажав на место на карте получите больше информации об этом месте.  [Сайт](http://evv71.pythonanywhere.com/)

![alt text](example.gif)

### Как установить

- Python3 должен быть уже установлен.
- Склонируйте репозиторий на свой компьютер.
```commandline
git clone https://github.com/Alex-mint/where_to_go.git
```  
- Установите зависимости:
```commandline
pip install -r requirements.txt
```

### Переменные окружения

Создайте файл .env в корневой папке с кодом и запишите туда:
```python
SECRET_KEY=ваш_секретный_ключ
DEBUG=True or False 
```
### Запуск

Для запуска программы необходимо написать в терминале следующее:
```commandline
python3 manage.py migrate
python3 manage.py runserver
```
Перейти по ссылке: `http://127.0.0.1:8000`

### Загрузить данных

Для быстрого заполнения предусмотрена загрузка данных из json файлов:
```commandline
python3 manage.py load_place https://имя-файла.json
```
Файл json должен быть следующего формата:
```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```
Вы можете воспользоваться готовыми [JSON-файлами](https://github.com/devmanorg/where-to-go-places)
