## DiscordQuoteBot

Исходный код Discord-бота, предназначенного для сохранения цитат сообщений пользователей в виде скриншотов. Для генерации изображений используется открытая библиотека [imgkit](https://pypi.org/project/imgkit/).

### Установка
- Используя pip установите следующие библиотеки: `Pillow`, `Discord.py`
- Установите библиотеку [wkhtmltopdf](https://wkhtmltopdf.org/)
- Заполните файл настроек `config.py`. В поле wkhtmltoimage_path укажите путь до исполняемого файла wkhtmltoimage.exe

### Команды
1. new - создание новой цитаты используя существующее сообщение. "Ответьте" на интересующее сообщение без аргументов для вызова команды.
2. fake - создание цитаты от имени пользователя на сервере с любым текстом и датой. Требует 3 аргумента. <br>
Пример использования: `q!fake @Irval 29.06.2022 "Это текст для цитирования"` (кавычки обязательны)

Все цитаты будут публиковаться в указанном в конфиге канале.

### Пример работы
![image](https://user-images.githubusercontent.com/56792892/176447727-20743982-61b5-4970-a928-9ab879fb018e.png)

###### При поддержке форума SMM продвижения в социальных сетях - DataStock.biz.
