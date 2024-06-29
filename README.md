# **<h1 align="center">SHOP WEBSITE</h1>**
## Учасники команди: 
> Team members
- [Коцаба Анастасія / Kotsaba Anastasiia](https://github.com/AnastasiaKotsaba2010) 
- [Швелідзе Крістіна / Shvelidze Kristina ](https://github.com/KristinaShvelidze)
- [Федорова Христина / Fedorova Kristina](https://github.com/Krissfedor)
- [Сергієнко Валерія / Serhiienko Valeriia](https://github.com/Valeria2009Serhiienko)  
- [Легар Денис / Legar Denys](https://github.com/denysUwU)


## Опис проекту
> Description 
+ **Shop website** - це веб-застосунок, що надає змогу користувачам здійснювати онлайн покупки. На сайті можна переглядати товари, додавати у кошик та замовляти їх у потрібне місце. Якщо користувач є адміністратором, йому надається право редагувати опис продукту, а також додавати новий асортимент на сторінку. Усі дії відслідковуються
телеграм-ботом, доступ до якого має лише власник веб-магазину. Бот швидко допомагає знайти усіх користувачів та вміст їх кошиків, записаних у базу даних.

>Shop website - is a web application that enables users to make online purchases. On the website, you can view products, add them to the cart and order them at the right place. If the user is an administrator, he is given the right to edit the product description, as well as add a new assortment to the page. All actions are tracked by a
Telegram bot, which can only be accessed by the owner of the web store. The bot will quickly help you find all users and the contents of their carts stored in the database.

## [Демоверсія / Demo version](https://anastasiiakotcaba.pythonanywhere.com/)

## Корисність проекту 
> Usefulness
+ Цей проект корисний для новачків у веб-розробці, оскільки він охоплює всі основні аспекти створення повноцінного веб-сайту: від реалізації інтерфейсу користувача до роботи з базою даних. Він може бути використаний як основа для реальних проектів та замовлень, та є чудовою нагодою попрактикуватись у створенні flask-проектів. Отримавши знання, ви з легкістю зможете зробити повноцінний веб-магазин на замовлення.

> This project is useful for beginners in web development, as it covers all the main aspects of creating a full-fledged website: from implementing the user interface to working with the database. It can be used as a basis for real projects and orders, and is a great opportunity to practice creating flask projects. With the knowledge gained, you will easily be able to create a full-fledged customised web store.

## Як розпочати роботу з веб-магазином
> How to get started with a web store

 ### Необхідні модулі
> Required modules

- `flask`: фреймворк для створення веб-застосунків мовою програмування Python, що використовує шаблонізатор Jinja2. Модуль надає змогу створити 'каркас' веб-сайту з базовими можливостями.
    > A framework for creating web applications in the Python programming language that uses the Jinja2 templating tool. The module allows you to create a 'shell' website with basic features.

- `flask_SQLAlchemy, sqlite3`: робота з базою даних. Модулі дозволяють створювати нові бази даних та вносити у них змінити.
    > Working with the database. Modules allow you to create new databases and make changes to them.

- `flask_migrate`: модуль, що дозволяє проводити міграції (забезпечує успішне створення таблиць у базі даних). При записі даних у базу, обов'язково варто проводити міграції.
    > Allows you to carry out migrations (ensures the successful creation of tables in the database). When recording data in the database, it is absolutely necessary to carry out migrations.

- `flask_login`: управління сесіями зареєстованого користувача.
    > Management of registered user sessions.

- `flask_mail`: модуль, що надає можливості автоматичної відправки листа до електронної пошти користувача.
    > Provides the ability to automatically send a letter to the user's e-mail.

- `pandas`: модуль для читання excel файлу, де зберігаються дані про асортимент продуктів.
    > Reads an excel file, which stores data on the range of products.

- `openpyxl`: модуль надає можливість зручно додавати дані в кінець аркуша електронної таблиці.
    > Provides an opportunity to conveniently add data to the end of a spreadsheet sheet.
 
- `os`: модуль, що швидко знаходить абсолютний шлях до потрібного файлу.
    >  Quickly finds the absolute path to the desired file.

- `pyTelegramBotAPI (telebot)`: модуль, що дозволяє створювати телеграм бота за допомогою token-ключа, який генерує телеграм канал BotFather.
    > Allows you to create bot telegrams using a token key that generates telegram channel BotFather.

### Інструкція по локальному запуску проекту
> Instructions for running the project locally

+ Переконайтесь, що у папці з головним додатком файл _init_.py містить усі потрібні імпортовані змінні.
> Make sure that the _init_.py file in the main application folder contains all the necessary imported variables.
+ Спочатку з файлу urls.py повинно бути усе імпортовано, далі з файлу settings.py повинна бути імпортована змінна головного додатку
> First, everything should be imported from the urls.py file, then the main application variable should be imported from the settings.py file.
+ Правою кнопкою миші натиснути на папку з головним додатком, обрати Open in Integrated Terminal
> Right-click on the folder with the main application, select Open in Integrated Terminal
+ У терміналі прописати такі команди:
>In the terminal of the folder with the setting.py file, you should write the following commands:
   ```
   > flask --app settings db init - створюємо каталог migrations у проекті.
   - У цей каталог додаються файли, необхідні для відстеження змін у схемі бази даних.
   - Це потрібно зробити тільки один раз, коли ви починаєте працювати з Flask-Migrate у вашому проекті.

   > flask --app settings db migrate - створюємо новий файл міграції на основі змін у моделі бази даних.
   - Цей файл міграції відображає зміни, які було зробилено у моделях (наприклад, додавання нових комірок).

   > flask --app settings db upgrade - застосовуємо файли міграції до бази даних.
   - Команда оновлює структуру бази даних відповідно до змін у моделях.
   - Це команда, яку ви будете використовувати щоразу, коли ви хочете застосувати нові зміни до вашої бази даних.
   ```
### Інструкція по віддаленому запуску проекту
> Instructions for remote project launch

1. Виконати локальний запуск.
2. У браузері відкрити сайт **pythonanywhere**, створити аккаунт початківця (зареєструватись).
3. Підвердити email адресу.
4. Перейти у вкладку **Web**, створити новий веб-застосунок.
5. У модальному вікні, у розділі **Select a Python Web framework** обрати **Flask** та версію Python **3.10**.
6. Перейти у вкладку **Console** > **Bash**.
7. Створити віртуальне оточення, прописавши наступну команду у консолі:
   - ```mkvirtualenv (назва віртуального оточення) -- python = python 3.10```
8. Встановити усі необхідні модулі, які були використані у проекті:
   - ```pip install flask, flask_sqlalchemy, flask_migrate, flask_login, flask_mail, pandas, openpyxl, sqlite3, pyTelegramBotAPI```
9. Завантажити файли проекту: у bush-консолі прописати команди:
   
    -  ```pwd - дізнатись поточну директорію```
    - ```cd mysite - перейти у папку mysite```
    - ```git clone (посилання на git-репозиторій)```
     
 11. Перейти у вкладку **Web**, прогортати вниз до розділу **Code**:
     
     - ```У пунктах Source code та Working directory, вкінці шляху дописати: /mysite/(назва папки з проектом)```
     - ```Перейти на посилання у панкті WSGI configuration file```
     - ```У 16-ому рядку замінити flask_app на назаву папки з файлом setting.py, app замінити на назву змінної для створення усіх веб-додатків. Зберегти зміни```
     
13. У розділі **Virtualenv** вказати назву віртуального середовища.
14. Оновити сайт, натиснувши кнопку **Reload**.
15. Перейти за посиланням веб-додатку.
16. У випадку помилок запуску веб-застосунку, перейти у розділ **Log files**, у пункті **Error log** перейти за посиланням; виправити вказані помилки, оновити сайт.

> Perform a local run.
> In a browser, open the pythonanywhere website, create a beginner account (register).
> Verify your email address.
> Go to the Web tab, create a new web application.
> In the modal window that opens, in the Select a Python Web framework section, select Flask and Python 3.10.
> Go to the **Console** > **Bash** tab.
> Create a virtual environment by issuing the following command in the console:
 - mkvirtualenv (name of the virtual environment) -- python = python 3.10
> Install all the necessary modules used in the project:
  - pip install flask, flask_sqlalchemy, flask_migrate, flask_login, flask_mail, pandas, openpyxl, sqlite3, pyTelegramBotAPI
> Download the project files: write commands in the bush console:
 - pwd - find out the current directory
 - cd mysite - go to the mysite folder
 - git clone (link to the git repository)
 - Go to the Web tab, scroll down to the Code section:
> In the **Source code** and **Working directory** sections, at the end of the path add: **/mysite/(project folder name)**.
> Go to the link in the **WSGI configuration file** link
> In the 16th line, replace flask_app with the name of the folder with the setting.py file, and replace app with the name of the variable for creating all web applications. Save changes
> In the Virtualenv section, specify the name of the virtual environment.
> Refresh the site by clicking the Reload button.
> Follow the link of the web application.
> In case of errors in launching the web application, go to the Log files section, in the Error log item, click the link; correct the errors, refresh the site.

### Структура проекту 

- `shop`: **головний додаток**, у якому зберігається база даних з інформацією користувача. У файл urls.py підключають усі частини проекту - Blueprint-и, проводять міграції. У папці templates є головний html-шаблон - base.html
- `registration_page`: логіка сторінки реєстрації, папка містить модель **User**, що зберагіє дані зареєстрованих користувачів, взятих з форми реєстрації у папці template.
- `authorization_page`: логіка сторінки авторизації, у папці template є шоблон з формою авторизації (логін та пароль).
- `home_page`:  основна сторінка користувача, яка з'являється після реєстрації, містить посилання на усі інші сторінки веб-сайту.
- `shop_page`: сторінка з асортиментом товару, є модель **Product**, що зберігає усі товари на сторінці. Інформація про продукт зберігається в **excel-файлі** Product.xlsx.
- `cart`: сторінка корзини, у якій зберігаються усі бажані товари для оформлення замовлення. У файлі cart.html є форма для заповнення інформації про замовлення, дані зберігаються у моделі **Order**. Сторінка cart_2.html відображається лише після оформлення замовлення. Файл views.py відповідає за відправку листа на пошту, що оповіщає про оформлення нового замволення.
- `admin_page`: сторінка, що доступна лише користувачам, які мають у таблиці User **is_admin = 1**. Файл admin.html містить 4 форми, за допомогою них, на сторінці можна змінювати опис товару (картинку, ціну, ім'я, знижку продукту), додавати новий асортимент товару та видаляти продукт з бази даних.
- `contacts_page`: сторінка, що відповідає за контакти, де ви можете зв'язатись із розробником сайту.
  
### Створення головного додатку: Flask

1. Створити змінну з назвою вашого головного додатку, що приймає у собі клас Flask з модуля flask  
>1. Create a variable with the name of your main application that takes the Flask class from the flask module 
2. Вказати необхідні параметри, такі як:
   - `import_name`: вказати назву файлу, у якому створюється головний додаток
   - `template_folder`: вказати шлях до папки templates
   -  `instance_path`: вказати шлях, де буде зберігатись база даних
   -  `static_url_path`: вказати назву, за якою можна знайти сторінку на веб-сайті
>2. Specify the necessary parameters, such as:
   >- `import_name`: specify the name of the file in which the main application is created
   >- `template_folder`: specify the path to the templates folder
   >- `instance_path`: specify the path where the database will be stored
   >- `static_url_path`: specify the name by which the page can be found on the website
3. Імпортувати створенну змінну до файлу __init__.py
   
Приклад коду:
```python
# Імортуємо потрібні модулі для створення бази даних та міграцій, головного додатку
import flask, flask_sqlalchemy, flask_migrate, os

shop = flask.Flask(
    import_name= "settings", # назва файлу, у якому знаходиться змінна 
    template_folder= "shop/templates", # шлях до папки templates
    instance_path= os.path.abspath(__file__ + "/.."), # шлях, де буде зберігатись база даних
    static_url_path= '/shop/' # назва, за якою можна знайти сторінку на веб-сайті
)
```
>Code example:
```python
# Import the necessary modules to create the database and migrations, the main application
import flask, flask_sqlalchemy, flask_migrate, os

shop = flask.Flask(
    import_name= "settings", # name of the file where the variable is located 
    template_folder= "shop/templates", # path to the templates folder
    instance_path= os.path.abspath(__file__ + "/..."), # path where the database will be stored
    static_url_path= '/shop/' # the name by which you can find the page on the website
)
```



 ### Створення додатку сторінки: Blueprint
1. Імпортувати модуль **flask** для подальшої роботи
2. Створити змінну з назвою вашої сторінки
3. У змінну записати класс Blueprint з модулю flask. У классі потрібно задати ряд параметрів, таких як:
   - `name`: назва додатку сторінки 
   - `import_name`: назва пакету в якому створюєтся blueprint
   - `template_folder`: шлях до папки templates
   - `static_folder`: шлях до папки static
   - `static_url_path`: посилання за яким можна знайти сторінку на веб-сайті
4. Імпортувати створенну змінну до файлу _ _init_ _.py
 >### Creating a page application: Blueprint
>1. Import the **flask** module for further work
>2. Create a variable with the name of your page
>3. Write the Blueprint class from the flask module to the variable. In the class, you need to set a number of parameters, such as:
   >- `name`: the name of the page application 
   >- `import_name`: the name of the package in which the blueprint is created
   >- `template_folder`: path to the templates folder
   >- `static_folder`: path to the static folder
   >- `static_url_path`: link where you can find the page on the website
>4. Import the created variable to the file _ _init_ _.py

Приклад коду:

```python
# Імпортуємо для подальшої роботи модуль flask
import flask

shop_page = flask.Blueprint(
    name = 'shop_page', # назва додатку сторінки 
    import_name= 'shop_page', # назва пакету, у якому створюється змінна (аби в наступних параметрах скоротити шлях)
    template_folder= 'templates', # папка з шаблоном сторінки (абсолютний шлях не варто вказувати через назву пакету)
    static_folder= 'static', # папка зі стилями сторінки
    static_url_path= '/shop_page/' # посилання за яким можна знайти сторінку на веб-сайті
)
```
Code example:

```python
# Import the flask module for further work
import flask

shop_page = flask.Blueprint(
    name = 'shop_page', # name of the page application 
    import_name= 'shop_page', # the name of the package in which the variable is created (to shorten the path in the following parameters)
    template_folder= 'templates', # folder with the page template (do not specify the absolute path through the package name)
    static_folder= 'static', # folder with page styles
    static_url_path= '/shop_page/' # link where you can find the page on the website
)
```

### Спосіб налаштування Blueprint

1. До файлу urls.py імпортувати змінну з Blueprint-додатком та функцію відображення сторінки 
2. До імпортованої змінної додаємо функцію **add_url_rule**, що відповідає за маршрут до сторінки, з такими параметрами, як:
   - `rule`: шаблон URL, який буде оброблятися
   - `view_func`: функція обробки, яка буде викликана, коли запит буде надіслано за вказаним URL
   - `methods`: функція, що була записана у параметр **view_func**, буде викликана для методів, що вказані у цьому параметрі
3. Звернутись до змінної головного додатку та зареєструвати blueprint, за допомогою функції **register_blueprint**. У параметрах передати потрібний blueprint-додаток

Приклад коду:
```python
# З пакетуу потрібного Blueprint-додатку імпортуємо змінну та функцію відображення html-сторінки
from shop_page import shop_page, shop_render

# Імпортувати головний додаток
from .settings import shop

# До змінної головного додатку додаємо функцію add_url_rule, що відповідає за маршрут до сторінки (посилання)
shop_page.add_url_rule(
    rule='/shop_page/', # шаблон URL, який буде оброблятися
    view_func= shop_render, # функція відображення html-сторінки, яка буде викликана, коли запит буде надіслано за вказаним URL
    methods = ['GET', 'POST'] # функція, що була вказана у параметрі view_func буде викликатись за вказаними методами
)

# Реєструємо blueprint, за допомогою функції register_blueprint. У параметрах передати потрібний blueprint-додаток
shop.register_blueprint(blueprint= shop_page)
```

### Опис файлів setting, mail_config і login_manager

#### Settings.py

+ Файл **settings.py** налаштовує та ініціалізує веб-додаток за допомогою класу Flask, а також створює базу даних та проводить міграції.

1. Імпортуємо необхідні модулі: **flask**, **flask-SQLAlchemy** для роботи з базою даних, **flask-migrate** для керування міграціями та **os** для роботи з файловою системою.
2. Створюємо змінну головноо додатку. Та налаштовуємо її за інструкцією, вказаною у пункті **Створення головного додатку: Flask**.
3. Налаштовуємо підключення до бази данних **data.db** за допомогою модуля **flask_sqlalchemy**. 
4. Створюємо базу даних, яка буде прив'язана до головного додатку.
5. Створюємо міграції.

Приклад коду:
```python
# Імортуємо потрібні модулі для створення бази даних та міграцій, головного додатку
import flask, flask_sqlalchemy, flask_migrate, os

shop = flask.Flask(
    import_name= "settings", # назва файлу, у якому знаходиться змінна 
    template_folder= "shop/templates", # шлях до папки templates
    instance_path= os.path.abspath(__file__ + "/.."), # шлях, де буде зберігатись база даних
    static_url_path= '/shop/' # назва, за якою можна знайти сторінку на веб-сайті
)

# Налаштовуємо підключення до бази данних. Так як база даних є локальною у значення вказуємо лише назву бази
shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Створюємо базу даних та міграції, які будуть прив'язані до головного додатку.
db = flask_sqlalchemy.SQLAlchemy(app= shop)

# Міграції - успішний запис змін у базу даних (створення таблиць, їх редагування)
migrate = flask_migrate.Migrate(app= shop, db= db)
```

#### Mail_config.py

+ Файл **main_config** налаштовує автоматичну відправку листа до електронної пошти у веб-додатку, використовуючи flask-mail.

1. Імпортуємо головний додаток з файлу **settings.ру** та модуль **flask-mail** для роботи з ел.поштою
2. Створюємо змінну зі значенням пошти людини від якої буде відсилатись лист.
3. Налаштовуємо відправку листа: 
   - `['MAIL_SERVER']`: налаштування відправки ел. поштою з використанням модулю flask_mail через SMTP сервер gmail
   - `['MAIL_PORT']`: налаштовуємо порт для підключення до SMTP сервера.
   - `['MAIL_USE_TLS']`: надаємо можливість користуватись TLS.
   - `['MAIL_USERNAME']`: записуємо створенну змінну (відправник).
   - `['MAIL_PASSWORD']`: задаємо гугл пароль додатку.
4. Надсилаємо автоматичний лист за допомгою класу **Mail**. У параметраї вказуємо назву головного веб-застосунку, аби лист надсилався при запуску цього проекту

- **SMTP-сервер** використовується для отримання та надсилання листів на вказану адресу одержувача, використовуючи порт 25, 465 aбо 587.
- **TLS** — це протокол, який забезпечує безпеку зв'язку через комп'ютерну мережу.

Приклад коду:
```python
# Імпортуємо головний додаток 
from .settings import shop

# Імпортуємо модуль flask_mail для налаштування відправки листа на ел. пошту
import flask_mail

# У змінну address записуємо ел.пошту людини, від якої будуть надходити листи
address = 'vserhiienko212@gmail.com'

shop.config['MAIL_SERVER'] = 'smtp.gmail.com' # сервер, який здійснює надсилання ел. пошти через протокол SMTP
shop.config['MAIL_PORT'] = 587 # порт для підключення SMTP-серверу. У цьому випадку це 587

shop.config['MAIL_USE_TLS'] = True # сервер ел. пошти буде використовувати TLS для шифрування з'єднань.
shop.config['MAIL_USERNAME'] = address # вказуємо змінну зі збереженою поштою відправника
shop.config['MAIL_PASSWORD'] = 'wqwf xzgz eqrb ceyt' # задаємо пароль для облікового запису ел. пошти, який ваш додаток буде використовувати для відправки ел. листів через сервер ел. пошти.

mail = flask_mail.Mail(app=shop) # Надсилаємо автоматичний лист за допомгою класу **Mail**. У параметраї вказуємо назву головного веб-застосунку, аби лист надсилався при запуску цього проекту.
```

####  Login_manager.py

+ Файл **login_manager** використовується для налаштування системи авторизації користувачів у головному-додатку за допомогою пакету flask_login.

1. Імпортувати необхідний модуль **flask_login** для управління сеансами користувачів. Імпортувати головний додаток з файлу **settings.ру**, а також модель з усіма зареєстрованими користувачами, для взаємодії з таблицею користувачів у базі даних.
2. Задаємо секретний ключ. Він використовується для шифрування даних сеансів (безпечне з'єднання)
3. Створює об'єкт LoginManager і зв'язуємо його з головним додатком. LoginManager керує станом входу користувачів у додатку.
4.  Вказує Flask-Login, яку сторінку показувати, коли неавторизований користувач намагається отримати доступ до захищеної сторінки.
5.  Вказуємо декоратор, який реєструє функцію завантаження користувача. Функція повертає ID користувача, збереженого у сеансі.

Приклад коду:
```python
import flask_login # управління сеансами користувачів
from registration_page.models import User # взаємодія з таблицею зареєстрованих користувачів User у базі даних.
from .settings import shop # імпортуємо головний додаток

shop.secret_key = 'Задайте секретний ключ' # встановлюємо секретний ключ для головного-додатку. 
login_manager = flask_login.LoginManager(shop) # створюємо змінну від класу LoginManager, що керує станом входу користувачів у додатку.

login_manager.login_view = 'show_login' # вказуємо функцію відображення сторінки авторизації

@login_manager.user_loader # декоратор, який реєструє функцію завантаження користувача

def load_user(id): # створюємо функцію, яка приймає параметр id, для отримання id користувача
    return User.query.get(id) # виконуємо запит до бази даних для отримання id користувача. Якщо користувач існує, він повертається, інакше повертається None.
```

### Опис html-шаблонів та призначення кожної форми

- Кожен **клас** у будь-якого html-тегу створений для його отримання у потрібному **js-файлі**, а також для **стилізації** цього елементу.
- Функція **url_for()** застосовується для **підключення потрібних js-файлів, або стилів**. **Перший параметр** цього методу це статика додатку **(blueprint)**, тобто варто вказати назву blueprint-змінної, а потім її **статичний файл**. **Другий параметр це шлях**: назва папки, у якій знаходиться потрібний файл та назва самого файлу.

### **Base.html** 
- Це шаблон базової сторінки для веб-сайту, який використовується як основа для інших HTML-сторінок. Використовуючи шаблони Jinja2, можна визначити загальну структуру HTML-документа і включати специфічний контент для різних сторінок.

Код шаблону:
```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    # Шаблон Jinja, що надає змогу динамічно вказувати назву сторінки у різних HTML-шаблонах
    <title>{% block title %} {% endblock %}</title> 

    # Блок, що дозволяє дочірнім (іншим) HTML-шаблонам мати власне посилання на css-файл
    {% block link %} {% endblock %}
</head>
    <body>
        # Блок, що дозволяє дочірнім (іншим) HTML-шаблонам мати свій особистий контент
        {% block content %}
        {% endblock %}
    </body>
</html>
```
### **Reg.html**: 
- Шаблон сторінки реєстрації

Код шаблону:
```html
# Цей шаблон наслідує базовий шаблон base.html, тобто вміст цього шаблону буде вставлений у відповідні блоки файлу base.html.
{% extends "base.html" %} 

# Встановлюємо заголовок сторінки "RegistrationPage" 
{% block title %} RegistrationPage {% endblock %}

# Знову через Jinja-блок динамічно підключаємо стилі для цього шаблону, а саме файл reg.css
{% block link %}
    # Функція url_for використовується для створення URL до статичного файлу (reg.css).
    <link rel="stylesheet" href="{{ url_for('registration.static', filename = 'css/reg.css')}}">
{% endblock %}

# Динамічно задаємо вміст сторінки через Jinja-блок
{% block content %}
    # Перевіряємо, чи є користувач зареєстрований через змінну is_registration, що передається до серверу через файл view.py
    {% if not is_registration %}
        # Якщо користувач не зареєстрований, то відображається форма, де варто вказати персональні дані
        <div class="container">
            # post-метод означає, що дані форми будуть відправлені на сервер для обробки
            <form method = 'post'>

                # Кожен тег input має своє призначення, на це вказує тег label
                <br><label for="name">Login</label>
                # Поле для введення логіна користувача. 
                # name="name" вказує, що дані з цього поля будуть надіслані на сервер під ключем "name".
                <br><input type="text" name="name"><br>

                <br><label for="email">Email<label>
                # Поле для введення електронної пошти
                <br><input type="text" name="email"><br>
                    
                <br><label for="password">Password<label>
                # Поле для введення пароля
                <br><input type="text" name="password"><br>

                <br><label for="password_confirmation">Password confirmation<label>
                # Поле для підтвердження пароля
                <br><input type="text" name="password_confirmation"><br>

                <div class="button">
                    # Кнопка відправки форми. Вона має тип submit, що вказує браузеру відправити дані форми на сервер при натисканні
                    <br><button type="submit" class="send-button">SEND</button>
                </div>           
            </form>          
        </div>
    {% else %}
        # В інакшому випадку, буде повідомлятись, що ми вже зареєстровані, а також div з посиланням на сторінку авторизації
        <h3 class="message">Ви вже зареєстровані</h3>
        <div style='text-align: center; margin-top: 15px; margin-right: 10px;'>
            <a href="/authorization_page/" class="reg-a">AUTHORIZATION</a>
        </div> 
    {% endif %}
{% endblock %}
```
+ Форма була створення для реєстрації користувача. Варто ввести ім'я, ел. пошту та пароль, аби успішно перейти на веб-додаток. Дані з форми обробляються через файл **veiw.py**, та зберігаються у таблицю **User**.

### **Login.html**: 
- Шаблон сторінки авторизації

Код шаблону:
```html
{% extends "base.html" %} # Наслідуємо базовий шаблон base.html

# Динамічно вказуємо назву сторінки - AuthorizationPage
{% block title %} AuthorizationPage {% endblock %}

# За допомогою Jinja-блоку завантажуємо файл login.css зі стилями сторінки 
{% block link %}
    # Функція url_for використовується для створення URL до статичного файлу (login.css).
    <link rel="stylesheet" href="{{ url_for('login.static', filename = 'css/login.css')}}">
{% endblock %}

# Задаємо вміст сторінки через Jinja-блок
{% block content %}
    # Div створений для посилання, за яким можливо перейти на сторінку авторизації
    <div style='text-align: right; margin-top: 15px; margin-right: 10px;'>
        <a href="/authorization_page/">AUTHORIZATION</a>
    </div> 

    <div class="login-container">
        # Форма авторизації, post-метод означає, що дані форми будуть відправлені на сервер для обробки за методом post
        <form method="post">
            # Поле для введення логіна або email, за якими користувач був зареєстрованим
            <br><label for="name">Login or email</label>
            <br><input type="text" name = 'name'><br>

            # Поле для введення паролю, за яким користувач зареєструвався
            <br><label for="password">Password</label>
            <br><input type="text" name = 'password'><br>

            <div class="button">
                 # Кнопка відправки форми. Вона має тип submit, що вказує браузеру відправити дані форми на сервер при натисканні
                <br><button type= 'submit'>SEND</button><br>
            </div>
        </form>
    </div>
{% endblock %}
```
+ Форма авторизації була створена для забезпечення функціоналу авторизації користувачів у веб-додатку. Основна мета цієї форми — дозволити користувачеві ввести свої дані (логін або email та пароль) для отримання доступу до покупок на сайті.

### **Home.html**
- Шаблон головної сторінки, яка доступна лише авторизованим користувачам. Її ціль - допомгати швидко знаходити потрібний додаток, наприклад сторінка з асортиментом товару

Код шаблону:
```html
{%  extends "base.html" %} # Наслідуємо базовий шаблон base.html

# Динамічно вказуємо назву сторінки - HomePage
{% block title %}
    HomePage
{% endblock %}

# За допомогою Jinja-блоку та функції url_for завантажуємо файл home.css зі стилями сторінки 
{% block link %}
    <link rel="stylesheet" href="{{ url_for('home.static', filename = 'css/home.css' )}}">
{% endblock %}

{% block content %}
    <h1>HOME PAGE</h1>

    # Перевіряємо, чи є користувач адміністратором через змінну is_admin, яка створенна у файлі views.py кожного веб-додатку. Також перевіряємо чи користувач зареєстрований, через змінну    
    # is_auth, якщо так - є доступ до усіх сторінок, якщо ж ні, то отримуємо посилання на авторизацію чи реєстрацію 
    {% if is_auth == True %}
        <div style=' text-align: left; margin-top: 15px; margin-left: 10px;'>
            <a href="/" style="font-weight: bolder" >HOME</a>
            <a href="/shop_page/"  style="text-decoration: none">SHOP</a>
            <a href="/cart/" class="basket-link" style="text-decoration: none">CART</a>
            <a href="/contacts/" style="text-decoration: none">CONTACTS</a> 

            <p>{{name}}</p>

            {% if is_admin %}
                # Якщо користувач є адміністратором, то є доступ до усіх сторінок, у тому числі й до сторінки admin. В іншому випадку, замість посилання на сторінку admin, відображається текст                  # You're not admin
                <a href="/admin/" style="text-decoration: none">ADMIN</a>
            {% else %}
                <p>You're not admin</p>
            {% endif %}
        </div> 

    {% else %} 
        <div style=' text-align: right; margin-top: 15px; margin-right: 10px;'>
            <a href="/registration_page/" style="font-size: 16.5px;">REGISTRATION</a>
            <a href="/authorization_page/" style="font-size: 16.5px; margin: 25px">AUTHORIZATION</a>
        </div>
    {% endif %}
{% endblock %}
```

### **Cart.html**
- Шаблон корзини. Сторінка містить в собі усі додані товари, можна самостійно редагувати к-сть товару: кнопками + та -

Код шаблону:
```html
{%  extends "base.html" %}
{% block title %}
    CartPage
{% endblock %}
{% block link %}
    <link rel="stylesheet" href="{{ url_for('cart.static', filename = 'css/basket.css' )}}">
{% endblock %}

{% block content %}
    <div class="links">
        <a href="/" style="text-decoration: none">HOME</a>
        <a href="/shop_page/" style="text-decoration: none">SHOP</a>
        <a href="/cart/" class="basket-link" style="font-weight: bolder">CART</a>
        <a href="/contacts/" style="text-decoration: none">CONTACTS</a> 

        <p>{{name}}</p>

        {% if is_admin %}
            <a href="/admin/" style="text-decoration: none">ADMIN</a>
        {% else %}
            <p>You're not admin</p>
        {% endif %}
    </div>

    # Перевіряємо, чи існують продукти на сторінці
    {% if products %}
        # Якщо на сторінці є товари, то за допомогою циклу for відображаємо картинку, ім'я, ціну та к-сть товару, яку можна змінювати кнопками + та - (логіка кнопок прописана у файлах 
        # plusCookies.js і deleteCookies.js).
        {% for product in products %}
            <div id = 'product-{{ product.id }}'>
                <br><img src= "{{ url_for('shop_page.static', filename= 'img/' + product.name + '.png') }}" alt="{{ product.id }}" class="product-img" ><br>                 
                <div class="text-conteiner">
                    <div class="name-space">
                        <p class="name">{{ product.description }} </p>
                    </div>
                    
                    <div class="amount">
                        <button class= "minus" id = "{{ product.id }}">-</button>
                        <p class="count">{{ product.count }}</p>
                        <button class= "plus" id = "{{ product.id }}">+</button>

                        <p class="price">{{ product.final_price }} грн</p>
                    </div>
                </div>

            </div>
        {% endfor %}

        # Div, що відповідає за оформленння товару, а також інформацію про загальну суму товару
        <div class="processing-conteiner">
            <br><button class="processing">ПЕРЕЙТИ ДО ОФОРМЛЕННЯ</button>

             # Теги на сторінці є порожніми, адже їх текст динамічно додається через файл processing.js
            <br><p class="final-count-num"></p>
            <p class="total-count">-товарів на суму</p>

            <p class="final-count"></p>

            <br><p class="total-discount">Знижка</p>
            <p class="final-discount"></p>
            
            <br><p class="total-price">Загальна сума</p>
            <p class="final-price"></p>
        </div>

        <div class="popup-processing" style= "display: none;">
            # Форма для оформлення замовлення, що з'являється лише по натисканню на кнопку 'Оформити замовлення'. Її головне призначення - заповнення даних, аби на ел.пошту користувача прийшов              # лист про нове замовлення товару, method="post" дає зрозуміти, що дані форми будуть відправлені на сервер для обробки за методом post
            <form method="post" class="processing-form">
                <p>ОФОРМЛЕННЯ ЗАМОВЛЕННЯ</p>

                <label for="name">ІМ'Я:</label>
                <input type="text" name="name">

                <label for="name">ПРІЗВИЩЕ:</label>
                <input type="text" name="last-name">
                
                <label for="name">ТЕЛЕФОН ЗАМОВНИКА:</label>
                <input type="tel" name="phone">
                
                <label for="name">EMAIL ЗАМОВНИКА:</label>
                <input type="email" name="email">
                
                <label for="name">МІСТО ОТРИМУВАЧА:</label>
                <input type="text" name="city">
                
                <label for="name">ВІДДІЛЕННЯ НОВОЇ ПОШТИ:</label>
                <input type="text" name="post-office">
                
                <label for="name">ДОДАТКОВІ ПОБАЖАННЯ:</label>
                <textarea name="preferences"></textarea>

                # Кнопка, яка відправляє форму. Вона має тип submit, що вказує браузеру відправити дані форми на сервер при натисканні
                <button type="submit" class="processing-btn" name = 'send-order' value="send-order">SEND</button>
            </form>
        </div>
    {% else %}
        # У випадку, якщо корзини немає, то відображається текст - Корзина порожня
        <h2>Корзина порожня</h2>
    {% endif %} 

    # Підключення усіх потрібних js-файлів через функцію url_for
    <script src= "{{ url_for('cart.static', filename = 'js/deleteCookies.js') }}"></script>
    <script src= "{{ url_for('cart.static', filename = 'js/plusCookies.js') }}"></script>
    <script src= "{{ url_for('cart.static', filename = 'js/processing.js') }}"></script>
{% endblock %}
```
- Форма processing-form була створена для оформлення замовлення. Основна мета форми полягає в тому, щоб користувач міг ввести свої особисті дані та деталі замовлення для подальшої обробки. Після натискання кнопки "Send", дані будуть відправлені про замовлення будуть відправленні на ел.пошту користувачу, вказану у полі 'Email замовника'. У листі ви зможете побачити номер замовлення, ваші особисті дані: ім'я, прізвище, номер телефону, відділення нової пошти, місто та ваші додаткові побажання. 

### **Cart_2.html**
- Інший шаблон корзини, що відображається після заповнення форми замовлення. Сторінка створена для підтверження замовлення, де можна переглянути к-сть замовлених товарів, вартість усього замовлення. Є кнопка 'Відмінити замовлення', що повертає на сторінку cart.html, також на пошту приходить повідомлення про скасоване замовлення.

Код шаблону:
```html
{%  extends "base.html" %}

{% block title %}
    CartPage
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('cart.static', filename = 'css/cart-3.css' )}}">
{% endblock %}

{% block content %}
    <div class="links">
        <a href="/" style="text-decoration: none">HOME</a>
        <a href="/shop_page/" style="text-decoration: none">SHOP</a>
        <a href="/cart/" class="basket-link" style="font-weight: bolder">CART</a>
        <a href="/contacts/" style="text-decoration: none">CONTACTS</a> 

        <p>{{name}}</p>

        {% if is_admin %}
            <a href="/admin/" style="text-decoration: none">ADMIN</a>
        {% else %}
            <p>You're not admin</p>
        {% endif %}
    </div>
    # Додатковий тект, що дає користувачу змогу зрозуміти, що замовлення в процесі оформлення 
    <p class="processing-data">Ваші дані у обробці </p>
    <p class="processing-data-2">консультант зв’яжеться з вами для підтвердження замовлення</p>
    {% if products %}
        # Якщо продукти існують на сторінці, то за допомогою циклу for про товар буде відображатись така інформація як, картинка, ім'я та ціна товару, к-сть, яку вже не можна буде змінити       
        {% for product in products %}
            <br><div id="product-{{ product.id }}" class="text-container">
                <img src="{{ url_for('shop_page.static', filename= 'img/' + product.name + '.png') }}" alt="{{ product.id }}" class="product-img">

                <p class="name"> {{ product.description }} </p>
                <p class="count"> {{ product.count }} </p>
                <p class="price"> {{ product.final_price }} грн </p>
            </div>
        {% endfor %}

        # Форма не має великого застосування і створена лише для зручності (для правильного написання коду у views.py), її мета - скасовувати замовлення. 
        <form method="post">
            <p class="total-price-order">Загальна вартість замовлення:</p>
            <button type="submit" class="reject-order" value="cancel-order" name="cancel-order">ВІДМІНИТИ ЗАМОВЛЕННЯ</button>
        </form>
    {% else %}
        <h2>Корзина порожня</h2>
    {% endif %} 
{% endblock %}
```
- На цій сторінці форма не має широкого призначення. Вона лише допомагає у файлі views.py правильно надсилати лист про скасоване замовлення.

### **Admin.html**
- Цей шаблон створений для відображення панелі адміністратора, де адміністратор може бачити список продуктів, додавати нові продукти, редагувати існуючі та видаляти продукти. Він також дозволяє адміністратору керувати різними параметрами продуктів

Код шаблону:
```html
{% extends "base.html" %}

{% block title %}
    ShopPage
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('admin.static', filename = 'css/admin.css') }}">
{% endblock %}

{% block content %}    
    <div class="links">
        <a href="/" style="text-decoration: none">HOME</a>
        <a href="/shop_page/" style="text-decoration: none">SHOP</a>
        <a href="/cart/" class="basket-link" style="text-decoration: none">CART</a>
        <a href="/contacts/" style="text-decoration: none">CONTACTS</a> 

        <p>{{name}}</p>

        {% if is_admin %}
            <a href="/admin/" style="font-weight: bolder">ADMIN</a>
        {% else %}
            <p>You're not admin</p>
        {% endif %}
    </div>

    # Форма для додавання продукту
    <form method="post" class="add-form">
        # Форма містить текст 'Додати продукт', а також кнопку у вигляді плюса. 
        <p class="add-text">ДОДАТИ ПРОДУКТ</p>
        <button class="new-product">
            <img src="{{ url_for('admin.static', filename= 'img/add.png') }}" alt="" class="add-img">
        </button>
    </form>
    # Застосовуємо цикл for для відображення продуктів     
    {% for product in products %}
        <br><img src="{{ url_for('shop_page.static', filename = 'img/' + product.name + '.png') }}" alt="{{ product.name }}" class="product-img"><br>

        # Невелика кнопка поруч з картинкою продукту. Кожен параметр товару (ім'я, ціна, к-сть, та ж картинка) мають цю кнопку, що дозволяє змінювати ці параметри за допомогою форм
        <button id="{{ product.id }}" class="edit-img-btn">
            <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="edit-img" style="margin-top: 60px;"><br>
        </button>

        # Відображення вмісту продукту: ціна та кількість. Самі div-теги створені для зручної стилізації         
        <div class="text-conteiner"> 
            <div class="text-content">
                # Ім'я продукту та кнопка змінення цього ім'я
                <p class="name" >{{ product.name }} 
                    <button class= "edit-name" id="{{ product.id }}">
                        <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="edit-name-img">
                    </button>
                </p>

                # Ціна продукту та кнопка змінення ціни
                <p class="price">{{ product.price }} грн 
                    <button class="edit-price" id="{{ product.id }}">
                        <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="edit-price-img">
                    </button>
                </p>

                # Знижка продукту та кнопка змінення знижки. Змінюючи знижку, відповідно змінюється й фінальна ціна (логіка дій прописана у файлі views.py)
                <p class="discount">Знижка {{ product.discount }}% 
                    <button class="edit-discount" id="{{ product.id }}">
                        <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="edit-discount-img">
                    </button>
                </p>

                # Фінальна ціна продукту, яка рахується за ціною товару та знижкою 
                <p class="price-2">{{ product.final_price }} грн</p>
                <button type="submit" class="button" id = "{{ product.id }} ">КУПИТИ</button>

                # Ємність, яку також можна змінювати
                <p class="text-img">ЄМНІСТЬ:</p>
                <button type= 'submit' class="amount">128GB <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="amount-edit"></button>
                <button type= 'submit' class="amount">256GB <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="amount-edit"></button>
                <button type= 'submit' class="amount">512GB <img src="{{ url_for('admin.static', filename= 'img/edit.png') }}" class="amount-edit"></button> 
            </div>

            # Форма для видалення продукту
            <form method="post" class="del-product">
                <button name= 'del' class="stock" value="{{ product.id }}">ВИДАЛИТИ ТОВАР</button>
                <img src="{{ url_for('admin.static', filename= 'img/bin.png') }}" alt="" class="bin">
            </form>
            
        </div>
    {% endfor %}

    # Універсальна форма для зміни будь-якого тексту. У edit.js динамічно задається те, що треба змінювати. Вміст label, input та button тегів змінюється залежно від того, що варто змінити.
    <div class = "modal-window" style= "display: none;">
        <form class = "modal-form" method="post" enctype= "multipart/form-data">
            <label for="" class = "modal-label"></label>
            <input type="" accept="" name="" class="input-data">
            <button class="change-btn" type="submit" value="" name="set-changes">SEND</button>
        </form>
    </div>

    # Форма для створення нового продукту за вказанми даними в полях
    <div class="new-product-div" style="display: none;">
        <form method="post" class="new-product-form" enctype= "multipart/form-data">
            <p>NEW PRODUCT</p>

            <label for="">IMAGE PRODUCT:</label>
            <input type="file" name="img" accept= "image/*">

            <label for="">NAME PRODUCT:</label>
            <input type="text" name="name">

            <label for="">DESCRIPTION PRODUCT:</label>
            <textarea name="description" id=""></textarea>

            <label for="">PRICE PRODUCT:</label>
            <input type="number" name="price">

            <label for="">DISCOUNT PRODUCT:</label>
            <input type="number" name="discount">

            <label for="">COUNT PRODUCT:</label>
            <input type="number" name="count">

            <button type="submit" name="new-product" value="new">SEND</button>
        </form>
    </div>

    # Підключення файлу edit.js, для зміни
    <script src="{{ url_for('admin.static', filename= 'js/edit.js') }}"></script>
{% endblock %}
```
- Форма з класом **add-form** була створена для **додавання нового продукту**. Як тільки буде натиснута кнопка цієї форми, буде з'являтись нова форма з класом new-product-form.
- Форма для створення нового продкту з класом **new-product-form** надає змогу адміністратору **додати новий продукт та самострійно обрати усі параметри товару**: картинку, ім'я, ціна, знижка, опис та к-сть товару, тобто адміністратор має змогу повністю створювати свій унікальний товар та додавати його на сторінку з іншими товарами. Новий товар зберігається у базі даних.
- Форма для змінення будь-якого тексту з класом **modal-form** дозволяє адміністратору швидко **редагувати ім'я товару, ціну товару та його знижку**. Фінальна ціна автоматично рахується за рахунок підключеного файлу edit.js. Зміни параметрів товару зберігаються у базі даних. 
- Остання форма з класом **del-product** відповідно **видаляє потрібний продукт** зі сторінки та бази даних.

### **Shop.html**
- Цей файл шаблону створений для відображення сторінки магазину, де користувачі можуть переглядати і взаємодіяти з продуктами, що доступні для покупки. Він включає навігаційні посилання, інформацію про кожен продукт (назву, ціну, знижку, остаточну ціну, статус наявності, а також кнопки для купівлі продуктів та вибору ємності).

Код шаблону:
```html
{% extends "base.html" %}

{% block title %}
    ShopPage
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('shop_page.static', filename = 'css/shop.css') }}">
{% endblock %}

{% block content %}
    <div class="links">
        <a href="/" style="text-decoration: none">HOME</a>
        <a href="/shop_page/" style="font-weight: bolder">SHOP</a>
        <a href="/cart/" class="basket-link" style="text-decoration: none">CART</a>
        <a href="/contacts/" style="text-decoration: none">CONTACTS</a> 

        <p>{{name}}</p>

        {% if is_admin %}
            <a href="/admin/" style="text-decoration: none">ADMIN</a>
        {% else %}
            <p>You're not admin</p>
        {% endif %}

    </div>
    # Створюємо продукт через цикл for
    {% for product in products %}
            <br><img src="{{ url_for('shop_page.static', filename = 'img/' + product.name + '.png') }}" alt="" class="product-img"><br>
            # Вміст кожного продукту: ціна, знижка, ім'я та картинка, ємність
            <div class="text-conteiner">
                <div class="text-content">
                    <p class="name" >{{ product.name }}</p>
                    <p class="price">{{ product.price }} грн</p>
                    <p class="discount">Знижка {{ product.discount }}%</p>
                    
                    <p class="price-2">{{ product.final_price }} грн </p>

                    <button type="submit" class="button" id = "{{ product.id }} " name="{{ product.final_price }}"> КУПИТИ </button>
                
                    <p class="text-img">ЄМНІСТЬ: </p>
                    <button type= 'submit' class="amount">128GB</button>
                    <button type= 'submit' class="amount">256GB</button>
                    <button type= 'submit' class="amount">512GB</button>
                
                </div>
                # Інформуємо користувача про наявність товару за допомогою цього div-тегу
                <p class="stock">ТОВАР В НАЯВНОСТІ</p>
                <img src="{{ url_for('shop_page.static', filename= 'img/tick.png') }}" alt="" class="tick">
            </div>
    {% endfor %}
     # Підключаємо файл shop.js, який створює позначку з к-стю товарів біля посилання на сторінку cart, а також записує у cookies id кожного продукту, при натисканні на кнопку 'Купити'
    <script src="{{ url_for('shop_page.static', filename = 'js/shop.js') }}" defer></script> 
{% endblock %}
```

### **Contacts.html**
- Шаблон сторінки контактів. Сторінка порожня і має лише заголовок - 'Contact page'

Код шаблону:
```html
{% extends 'base.html' %}

{% block title %}
    ContactsPage
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('contacts.static', filename = 'css/contacts.css') }}">
{% endblock %}

{% block content %}
    <div class="links">
        <a href="/" style="text-decoration: none">HOME</a>
        <a href="/shop_page/" style="text-decoration: none">SHOP</a>
        <a href="/cart/" class="basket-link" style="text-decoration: none">CART</a>
        <a href="/contacts/" style="font-weight: bolder">CONTACTS</a> 

        <p>{{name}}</p>

        {% if is_admin %}
            <a href="/admin/" style="text-decoration: none">ADMIN</a>
        {% else %}
            <p>You're not admin</p>
        {% endif %}

    </div>

    <h1>Contacts Page</h1>
{% endblock %}
```

### Опис кожного файлу views.py у всіх веб-додатках
### **Shop_page**
- Цей файл був створений для завантаження даних про продукти з Excel-файлу у базу даних, якщо база даних порожня, а також для відображення веб-сторінки магазину, де користувачі можуть переглядати список продуктів. Якщо користувач є адміністратором і автентифікований, йому надається додаткова інформація та функції управління.

Код файлу:
```python
# Імпортуємо бібліотеки: flask для веб-додатків, pandas для роботи з табличними даними і os для роботи з файловою системою.
import flask, os, pandas
# Імпорт бази даних з головного проекту 
from shop.settings import db
# Імпорт моделі Product для роботи з продуктами в базі даних.
from .models import Product
# Імпорт current_user для отримання інформації про поточного користувача.
from flask_login import current_user

def shop_render():
    # Умова, що перевіряє відсутність продуктів в базі даних: 
    if len(Product.query.all()) == 0:
        # Отримання абсолютного шляху до таблиці Product.xlsx
        path = os.path.abspath(__file__ + '/../Product.xlsx')

        # Читаємо excel-файл за допомогою pandas, функції read_excel
        read_xl = pandas.read_excel(
            io= path, # шлях до таблиці
            header= None, # вказівка, що файл не містить заголовків.
            names = ['name', 'price', 'count', 'discount', 'description', 'final_price'] # імена комірок у моделі Product
        )

        # Ітерація по рядках DataFrame за допомогою циклу for:
        for row in read_xl.iterrows():
            data_row = row[1] # у список записуємо кожен рядок з excel-файлу 

            # У зміну product записуємо дані з моделі Product
            product = Product( 
                name = data_row['name'], # у комірку name записуємо ім'я продукту, яке було вказано в excel-файлі
                price = data_row['price'], # у комірку price записуємо ціну продукту, яке було вказано в excel-файлі
                count = data_row['count'], # у комірку count записуємо к-сть продуктів, яке було вказано в excel-файлі
                discount = data_row['discount'], # у комірку discount записуємо знижку продукту, яке було вказано в excel-файлі
                description = data_row['description'], # у комірку description записуємо опис продукту, яке було вказано в excel-файлі
                final_price = data_row['final_price'] # у комірку final_price записуємо фінальну ціну продукту, що рахується на основі знижки та 
                # початкової ціни
            )
            db.session.add(product) # додаємо об'єкт в базу даних.
        db.session.commit() # записуємо зміни у базу даних.

    is_admin = False # якщо користувач не є адміністратором.
    if current_user.is_authenticated: # Умова, що перевіряє чи є користувач авторизованим
        return flask.render_template( # рендеринг шаблону сторінки shop.html
            template_name_or_list = "shop.html", # повертаємо сторінку shop.html
            products = Product.query.all(), # отримуємо усі продукти з моделі Product
            is_auth = current_user.is_authenticated, # передаємо це як параметр перевірки авторизації, для подальшого використання у shop.html
            name = current_user.name, # додаємо ім'я зареєстрованого користувача 
            is_admin = current_user.is_admin, # передаємо це як параметр перевірки адміністраторських прав, для подальшого використання у shop.html
        )
    return flask.render_template( # Якщо користувач не є авторизованим, то відбувається рендеринг сторінки shop.html, проте без певних параметрів
        template_name_or_list = "shop.html", # повертаємо сторінку shop.html
        products = Product.query.all(), # отримуємо усі продукти з моделі Product
        is_admin = is_admin # передаємо змінну зі значенням False, адже комірка is_admin може мати значення лише піся авторизації користувача
    )
```

### **Reg_page**
-

Код файлу:
```python
# Імпортуємо потрібні модулі та файли
import flask, os, json
from shop.settings import db
from flask_login import current_user
## Імпорт моделі User для роботи з даними користувача в базі даних.
from .models import User

def reg_render():
    # Створюємо змінну для перевірки, чи є користувач зареєстрованим
    is_registration = False

    # Умова, що перевіряє чи надсилаються ґякісь дані з форми
    if flask.request.method == "POST":
        #
        try:
            # Додаємо нового користувача в базу даних:
            user = User(
                name = flask.request.form['name'], # отримуємо дані з форми, а саме input з ім'ям, та записуємо у базу даних у визначену комірку.
                email = flask.request.form['email'], # отримуємо дані з форми, а саме input з ел. листом, та записуємо у базу даних.
                password = flask.request.form['password'], # отримуємо дані з форми, а саме input з паролем, та записуємо у базу даних.
                password_confirmation = flask.request.form['password_confirmation'], # отримуємо дані з форми, а саме input з паролем, та записуємо у базу 
                даних. 

                is_admin = False # Задаємо, що усі зареєстровані користувачі не будуть адміністраторами. Змінити значення можна лише вручну, або через 
                # телеграм бота. Це може робити лише власник веб-сайту.
            )

            db.session.add(user) #
            db.session.commit() #
            is_registration = True #

        except Exception as e: 
            print(e) #
    if not current_user.is_authenticated: #
        #
        return flask.render_template(template_name_or_list= 'reg.html', is_registration= is_registration, content = data_dict['content'])
    else:
        print('auth')
        return flask.redirect('/authorization_page/') #
```
### **admin_page**
Код файлу:

    import flask, os, pandas
    # Імпортуються необхідні модулі Flask, os та pandas
    
    from shop.settings import db
    # Імпортується об'єкт бази даних з налаштувань додатку
  
    from shop_page.models import Product
    # Імпортується модель Product з файлу models додатку shop_page
    
    from registration_page.models import User
    # Імпортується модель User з файлу models додатку registration_page
    
    from flask_login import current_user
    # Імпортується об'єкт current_user для роботи з автентифікацією
    
    def admin_render():
        if len(Product.query.all()) == 0:
            # Перевірка, чи є продукти у базі даних. Якщо немає, виконується завантаження даних з файлу Excel
    
            path = os.path.abspath(__file__ + '/../Product.xlsx')
            # Визначення абсолютного шляху до файлу Excel з продуктами
    
            read_xl = pandas.read_excel(
                io=path,
                header=None,
                names=['name', 'price', 'count', 'discount', 'description']
            )
            # Зчитування файлу Excel за допомогою pandas, задаються назви стовпців для зчитаних даних
    
            for row in read_xl.iterrows():
                data_row = row[1]
                # Перебір кожного рядка з файлу Excel
    
                product = Product(
                    name=data_row['name'],
                    price=data_row['price'],
                    count=data_row['count'],
                    discount=data_row['discount'],
                    description=data_row['description'],
                    final_price=data_row['final_price']
                )
                # Створення нового об'єкта Product для кожного рядка
    
                db.session.add(product)
                # Додавання продукту до сесії бази даних
    
            db.session.commit()
            # Збереження змін у базі даних
    
        if flask.request.method == 'POST':
            # Перевірка, чи є запит методом POST.
    
            if flask.request.form.get('del'):
                # Обробка форми видалення продукту
    
                product_id = int(flask.request.form['del'])
                product_del = Product.query.get(product_id)
                # Отримання продукту за його ID
    
                if product_del:
                    db.session.delete(product_del)
                    db.session.commit()
                    # Видалення продукту з бази даних та збереження змін
    
                    os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/img/{product_del.name}.png"))
                    # Видалення зображення продукту з файлової системи
    
            if flask.request.form.get('new-product'):
                # Обробка форми додавання нового продукту
    
                product = Product(
                    name=flask.request.form['name'],
                    price=flask.request.form['price'],
                    count=flask.request.form['count'],
                    discount=flask.request.form['discount'],
                    description=flask.request.form['description'],
                    final_price=round(int(flask.request.form['price']) - (int(flask.request.form['price']) * (int(flask.request.form['discount']) / 100)), 0)
                )
                # Створення нового продукту, обчислення кінцевої ціни з урахуванням знижки
    
                db.session.add(product)
                db.session.commit()
                # Додавання продукту до бази даних та збереження змін
    
                img = flask.request.files['img']
                img.save(os.path.abspath(__file__ + f'/../../shop_page/static/img/{product.name}.png'))
                # Збереження зображення продукту у файловій системі
    
            if flask.request.form.get('set-changes'):
                # Обробка форми зміни даних продукту
    
                product_data = flask.request.form.get("set-changes").split('-')
                product_id = int(product_data[-1])
                get_product = Product.query.get(product_id)
                # Розбивка даних форми на тип зміни та ID продукту, отримання продукту за ID
    
                abspath = os.path.abspath(__file__ + "/../../shop_page/static/img")
    
                if "image" == product_data[0]:
                    # Зміна зображення продукту
    
                    os.remove(abspath + f'/{get_product.name}.png')
                    new_image = flask.request.files['image']
                    new_image.save(abspath + f'/{get_product.name}.png')
                    # Видалення старого зображення та збереження нового
    
                elif 'name' == product_data[0]:
                    # Зміна назви продукту
    
                    new_product_name = flask.request.form['name']
                    os.rename(src=abspath + f'/{get_product.name}.png', dst=abspath + f'/{new_product_name}.png')
                    get_product.name = new_product_name
                    db.session.commit()
                    # Оновлення імені файлу зображення та назви продукту у базі даних
    
                elif 'price' == product_data[0]:
                    # Зміна ціни продукту
    
                    new_product_price = flask.request.form['price']
                    get_product.price = new_product_price
                    get_product.final_price = round(int(new_product_price) - (int(new_product_price) * (int(get_product.discount) / 100)), 0)
                    db.session.commit()
                    # Оновлення ціни та кінцевої ціни продукту у базі даних
    
                elif 'discount' == product_data[0]:
                    # Зміна знижки продукту
    
                    new_product_discount = flask.request.form['discount']
                    get_product.discount = new_product_discount
                    get_product.final_price = round(int(get_product.price) - (int(get_product.price) * (int(new_product_discount) / 100)), 0)
                    db.session.commit()
                    # Оновлення знижки та кінцевої ціни продукту у базі даних
    
        if current_user.is_authenticated:
            # Перевірка, чи користувач автентифікований
    
            return flask.render_template(
                template_name_or_list='admin.html',
                products=Product.query.all(),
                is_auth=current_user.is_authenticated,
                name=current_user.name,
                is_admin=current_user.is_admin
            )
            # Повернення шаблону admin.html з даними про всі продукти та даними про користувача для відображення на сторінці
### **cart_page**
```python
Функція cart_render обробляє відображення сторінки кошика покупок у веб-додатку на Flask, керуючи як відображенням продуктів, так і обробкою замовлень. Нижче наведено пояснення функції та її компонентів:

1. Імпорт модулів:
    - Необхідні модулі Flask (`flask`, `flask_mail`).
    - current_user з flask_login для доступу до інформації про поточного користувача.
    - Моделі Product та Order для взаємодії з базою даних.
    - db для операцій з базою даних.
    - mail для відправки електронної пошти.
    - telegram_bot для відправки повідомлень через Telegram.

2. Визначення функції: cart_render
 is_admin = False - Якщо користувач не адміністратор
    products_cookie = flask.request.cookies.get('products') - Перевірка наявності продуктів у куках:

         if products_cookie:  - Отримує куки products.
          products = products_cookie.split(' ') - Розділяє куки для отримання окремих ID продуктів.
             list_products = []- Ініціалізує list_products для зберігання об'єктів продуктів.
repeate_id = []-  для відстеження оброблених ID продуктів.

    for id_product in products: - Підрахунок продуктів:
     count_products = products.count(id_product) - Перебирає ID продуктів для підрахунку кількості.
if id_product not in repeate_id:
product = Product.query.get(id_product)  - Отримує деталі продуктів з бази даних.
        if product: 
product.count = count_products 
list_products.append(product) repeate_id.append(id_product)- Додає об'єкти продуктів з їх кількістю до list_products.

    - Обробка POST запитів:
        if flask.request.method == 'POST': - Якщо метод запиту є POST.
         if flask.request.form.get('send-order'):  - Якщо форма містить send-order, створює новий об'єкт Order з даними форми.
 
order = Order(
                name=flask.request.form['name'] - записуємо імʼя з форми яку користувач заповнює на сайті.
                last_name=flask.request.form['last-name']  - записуємо призвіще з форми яку користувач заповнює на сайті.
                    phone=flask.request.form['phone']  - записуємо телефон з форми яку користувач заповнює на сайті.
                email=flask.request.form['email']  - записуємо електронну пошту з форми.
                city=flask.request.form['city']  - записуємо місто з форми.
               post_office=flask.request.form['post-office']  - записуємо значення з форми.
            preferences=flask.request.form['preferences']  - записуємо значення з форми.
            id_product=str(list_products) - в зміну записуємо всі продукти з списку list_products
            )

            db.session.add(order) - Додає замовлення до бази даних.
db.session.commit() - Збереження змін у базі даних.     
   
message_text = f'Order № {order.id}: \n\n'  - в змінну message_text записуємо id ордеру. \n - переходить на наступний рядок.
message_text += f'First name: {order.name}\n' - += до рядку вище додає нове значення, імʼя, із змінної order  в яку записане значення імʼя яке взяте із форми.
message_text += f'Last name: {order.last_name}\n' - записуємо прізвище.
message_text += f'Phone number: {order.phone}\n' - записує номер телефону.
message_text += f'Email: {order.email}\n' записує електронну адресу.
message_text += f'City: {order.city}\n' - записуж назву міста.
message_text += f'Post office: {order.post_office}\n' - записує поштове відділення.
message_text += f'Preferences: {order.preferences}\n' - записує додаткові побажання.


message = flask_mail.Message(
subject=f'Order № {order.id}', 
sender='vserhiienko212@gmail.com', 
recipients=[f'{order.email}'], 
body= message_text ) mail.send(message) - Створює повідомлення з підсумком замовлення.

mail.send(message) - Відправляє електронного листа з підтвердженням замовлення користувачу.
            
@telegram_bot.callback_query_handler(func=lambda callback: True) 
def answer(callback): 
telegram_bot.send_message( 
callback.message.chat.id, 
text=f'Було зроблено нове замовлення №{order.id}', 
message_thread_id= 2 ) - Відправляє сповіщення у Telegram чат.

return flask.render_template( 
template_name_or_list='cart_2.html', 
is_admin=current_user.is_admin,
name=current_user.name, 
products=list_products,
is_authenticated=current_user.is_authenticated
)  - Відображає інший шаблон кошика (`cart_2.html`), що вказує на розміщення замовлення.
        
elif flask.request.form.get('cancel-order'):

cancelled_message_text = f'Order was cancelled' 

cancelled_message = flask_mail.Message(  -Скасування замовлення:
subject=f'Order',
sender='vserhiienko212@gmail.com', 
recipients=[current_user.email], 
body=cancelled_message_text
 ) 

mail.send(cancelled_message) 
print('order was cancelled')  - Якщо форма містить cancel-order, відправляє електронного листа зі скасуванням замовлення користувачу.

return flask.render_template(
template_name_or_list='cart.html',
 is_admin=current_user.is_admin,
 name=current_user.name,
 products=list_products,
 is_authenticated=current_user.is_authenticated
 ) 
        - Відображає сторінку кошика знову (`cart.html`).

 if current_user.is_authenticated:
 return flask.render_template( 
template_name_or_list = 'cart.html',
products= list_products,
is_authenticated = current_user.is_authenticated, 
name = current_user.name, 
is_admin = current_user.is_admin
 )
        - Якщо користувач аутентифікований, відображає шаблон кошика (`cart.html`) з деталями продуктів і інформацією про користувача.

        - Якщо користувач не аутентифікований, відображає шаблон кошика без інформації про користувача.


    return flask.render_template( 
template_name_or_list = 'cart.html', 
is_admin = current_user.is_admin
 ) - Відображає відповідний шаблон на основі статусу аутентифікації користувача та дій форми.


```  

### Детальний опис кожного файлу models.py 
#### Models.py сторінки shop_page
Приклад створення моделі:
```python
# Імпортуємо базу даних 
from shop.settings import db
# Створюємо клас Product, що наслідує модель бази даних, це вказує на те, що це таблиця, яка буде створена у базі після міграцій
class Product(db.Model):
    # Створюємо комірку 'id', з типом даних 'Integer'. Параметр primary_key вказує, що кожен id є унікальним ключем кожного користувача. Id продукту
    # потрібне, аби додвати його у cookie файли. Таким чином можна буде зрозуміти, який саме товар ми додали у корзину, або ж який товар ми бажаємо     
    # видалити.
    id = db.Column(db.Integer, primary_key = True)

    # Створюємо комірку: 'name' з типом даних 'String' довжиною до 50 символів, параметр nullable = False, вказує, що комірка не може бути порожньою
    name = db.Column(db.String(50), nullable = False)

    # Створюємо настпуні комірки: 'price', 'count', 'discount', 'description' з типом даних 'Integer', усі комірки не можуть бути порожніми
    price = db.Column(db.Integer, nullable = False)
    count = db.Column(db.Integer, nullable = False)
    discount = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Integer, nullable = False)
    final_price = db.Column(db.Integer, nullable = False)

    # Метод, що буде повертати id та ім'я продукту з бази даних
    def __repr__(self):
        return f"id: {self.id}; name: {self.name};"
```
- модель **Product** створена для продуктів. В моделі зберігаються усі необхідні товари, які в подальшому будуть відображатись на головній сторінці. Таблиця створена для зручності, щоб легко отримувати усі продукти з бази даних та використовувати це як параметр у функції render_template. Це надає можливість зручно відображати увесь асортимент товарів з бази даних у html-шаблонах через цикл for.

#### Models.py сторінки registration_page
Приклад створення моделі:
```python
# Імпортуємо базу даних 
from shop.settings import db
# Імпортуємо UserMixin до моделі User, тим самим забезпечуємо її зв'язок з модулем flask-login, що дозволяє легко керувати авторизацією користувачів.
# При імпортуванні UserMixin, до бази даних додається метод is_authenticated, що показує чи увійшов користувач у систему. 
from flask_login import UserMixin

# Створюємо клас User, що наслідує модель бази даних, це вказує на те, що це таблиця, яка буде створена у базі після міграцій.
# Додавання UserMixin дозволяє головному додатку знати, чи є користувач авторизованим.
class User(db.Model, UserMixin):
    # Створюємо комірку 'id', з типом даних 'Integer'. Параметр primary_key вказує, що кожен id є унікальним ключем кожного користувача. Тут id допомагає
    # боту зрозуміти, якого саме користувача видаляти з бази 
    id = db.Column(db.Integer, primary_key = True)

    # Створюємо настпуні комірки: 'name', 'email', 'password', 'password_confirmation' з типом даних 'String', усі комірки не можуть бути порожніми
    # Комірки створені для реєстрації користувача, ел. пошта вказується, аби в подальшому при оформленні замовлення на цю ел.пошту прийшов лист про 
    # замовлення. Ім'я користувача буде завжди відображатись, щоб показувати, під яким ім'ям увійшов користувач. Паролі використовуються для безпеки.
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    password_confirmation = db.Column(db.String(20), nullable = False)

    # Комірка, що вказує, чи користувач адміністратором. Якщо значення комірки 1, то це адміністротор, що має доступ до сторінки admin та може редагувати 
    # або додавати новий асортимент продукту. В інакшому випадку(значення комірки = 0) цих можливостей користувач мати не буде.
    is_admin = db.Column(db.Boolean)

    # Метод, що буде повертати ім'я користувача з бази даних
    def __repr__(self) -> str:
        return f"Ім'я користувача - {self.name}"
```
- Модель була створена для реєстрації користувачів. Після того, як користувач введе дані у форму реєстрації, вони будуть зберігатись у відповідних комірках моделі. Це надає можливість легко отримувати усіх користувачів або ж видаляти їх з бази даних для телеграм боту. На сторінці можна відображати ім'я користувача. І звісно модель допомагає для авторизації, де є перевірка комірок паролю та ім'я на схожість з зареєстрованими даними користувача.

#### Models.py сторінки cart
Приклад створення моделі:
```python
# Імпортуємо базу даних 
from shop.settings import db

Створюємо клас Order, що наслідує модель бази даних, це вказує на те, що це таблиця, яка буде створена у базі після міграцій
class Order(db.Model):  
    # Створюємо комірку 'id', з типом даних 'Integer'. Параметр primary_key вказує, що кожен id є унікальним ключем кожного користувача. Id потрібно, для 
    # того, щоб під час надсилання ел. листа на пошту користувач міг бачити номер замовлення
    id = db.Column(db.Integer, primary_key = True)

    # Створюємо настпуні комірки: 'name', 'last_name', 'phone', 'email', 'city', 'post_office', 'preferences', усі комірки не можуть бути порожніми
    # Комірки створені для того, щоб користувач зміг вказати усю необхідну інформацію про замовлення, ел. пошта вказується, аби в подальшому при оформленні 
    # замовлення на цю ел.пошту прийшов лист про здійснення замовлення, ім'я та прізвище допомагають зрозуміти, хто зробив замовлення.
    name = db.Column(db.String(60), nullable = False)
    last_name =  db.Column(db.String(60), nullable = False)
    phone =  db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(60), nullable = False)
    city = db.Column(db.String(60), nullable = False)
    post_office = db.Column(db.String(60), nullable = False)
    preferences = db.Column(db.String(60), nullable = False)

    # Комірка для id продукту, значення передається через файл veiws.py. Це допомагає зрозуміти, які продукти були замовлені
    id_product = db.Column(db.String(60), nullable = False)
    # Метод повернення id замовлення 
    def __repr__(self):
        return f'id: {self.id}'
```
- Модель було створено для збереження даних про замовлення. З її допомогою можна легко надіслати лист на вказану пошту у комірці 'email', з усією інформацією замовлення. Також замовлення можна відмінити.


### Що таке база даних?
- База даних — це місце, де зберігаються дані у впорядкованому вигляді, щоб їх було легко знайти, зберігати та використовувати. Це як великий електронний записник, де ви можете зберігати різну інформацію і потім швидко її знаходити. У нашому проекті ми додавали окремі таблиці, аби впорядкувати інформацію про користувача, товари та замовлення. У базі можна зручно змінювати значення, що додає їй функціональності. 

### Чому саме SQLite3?
- SQLite3 — це легка, вбудована, регуляційна база даних, яка не вимагає окремого серверного програмного забезпечення для свого функціонування. SQLite3 легко налаштувати та використовувати. Вона може працювати безпосередньо з файлом бази даних. Це є вбудована база даних, тобто не потребує окремого процесу або сервера. Дані в SQLite3 зберігаються у звичайному файлі, що робить їх легко доступними на різних платформах та пристроях. Це робить SQLite3 ідеальним вибором для проектів, які потребують простої і швидкої міграції даних. База використовує мінімум ресурсів, що робить її ідеальною для мобільних додатків, вбудованих систем та веб-додатків з невеликим навантаженням.

### Яку роль виконує ID у таблицях бази даних?
- Id - це унікальний ключ. Завдяки ньому, можна легко знайти конкретний запис у таблиці, це особливо корисно для пошуку, оновлення або видалення записів з бази. Завдяки унікальності ID забезпечується цілісність даних у базі даних, оскільки кожен запис має свій унікальний ідентифікатор, який можна використовувати для відстеження та керування даними. Комірка id у моделі Product дає можливість відслідковувати, який саме продукт було додано до корзини. Далі ці значення додаються до cookie-файлів, щоб легко змінювати к-сть товарів у корзині. Це також дає змогу адміністратору та телеграм боту видаляти продукт. Комірка id у моделі User допомагає боту видаляти користувачів з бази даних. Комірка id у моделі Order слугує номером замовлення.


### Опис кожного js-файлу у всіх веб-додатках
#### Файл admin
Редагування зображення: Цей блок коду додає обробник подій до кнопок з класом edit-img-btn. При натисканні на кнопку ми можемо завантажити нову картинку. Поле вводу налаштовується для прийому будь яких файлів зображень.

    let listButtonImage = document.querySelectorAll(".edit-img-btn")
    for (let count = 0; count < listButtonImage.length; count++) {
        let button = listButtonImage[count]
        button.addEventListener(
            type = "click",
            listener = (event) => {
                document.querySelector(".modal-window").style.display = "flex"

                let inputData = document.querySelector(".input-data")
                inputData.type = "file" 
                inputData.accept = "image/*"
                inputData.name = "image"
                document.querySelector(".modal-label").textContent = "CHANGE IMAGE:"
                document.querySelector('.change-btn').value = image-${button.id}
            }
        )
    }

Редагування назви: Цей блок додає обробник подій до кнопок з класом edit-name. При натисканні на кнопку ми можемо редагувати текст. Налаштовано під редагування тексту.

    let listButtonName = document.querySelectorAll(".edit-name")
    
    for (let count = 0; count < listButtonName.length; count++) {
        let button = listButtonName[count]
        button.addEventListener(
            type = "click",
            listener = (event) => {
                document.querySelector(".modal-window").style.display = "flex"
                let inputData = document.querySelector(".input-data")
                inputData.type = "text"
                inputData.name = "name"
                document.querySelector(".modal-label").textContent= "CHANGE TEXT:"
                document.querySelector('.change-btn').value = `name-${button.id}`
            }
        )
    }

Редагування ціни: Цей блок додає обробник подій до кнопок з класом edit-price. При натисканні на кнопку відкривається модальне вікно для зміни ціни. Поле вводу налаштовується для введення числових значень.

    let listButtonPrice = document.querySelectorAll(".edit-price")
    for (let count = 0; count < listButtonPrice.length; count++) {
        let button = listButtonPrice[count]
    
        button.addEventListener(
            type = "click",
            listener = (event) => {
                document.querySelector(".modal-window").style.display = "flex"
    
                let inputData = document.querySelector(".input-data")
                inputData.type = "number"
                inputData.name = "price"
                document.querySelector(".modal-label").textContent= "CHANGE PRICE:"
                document.querySelector('.change-btn').value = `price-${button.id}`
            }
        )
    }

Редагування знижки: Цей блок додає обробник подій до кнопок з класом edit-discount. При натисканні на кнопку відкривається модальне вікно для зміни знижки. Поле вводу налаштовується для введення числових значень.

    let listButtonDiscount = document.querySelectorAll(".edit-discount")
    for (let count = 0; count < listButtonDiscount.length; count++) {
        let button = listButtonDiscount[count]
        button.addEventListener(
            type = "click",
            listener = (event) => {
                document.querySelector(".modal-window").style.display = "flex"
                let inputData = document.querySelector(".input-data")
                inputData.type = "number"
                inputData.name = "discount"
                document.querySelector(".modal-label").textContent= "CHANGE DISCOUNT:"
                document.querySelector('.change-btn').value = `discount-${button.id}`
            }
        )
    }
Додаємо обробник подій на кнопку new-product, подією буде натискання на кнопку. event.preventDefault() Ця функція запобігає дефолтній поведінці кнопки, тобто щоб, дів, який буде з'являтись по натисканню кнопки не зникав через одну секунду.

    document.querySelector('.new-product').addEventListener(
        'click', (event) => {
            event.preventDefault()
            document.querySelector('.new-product-div').style.display = 'flex'
        }
    )

#### Файл PlusCookies(cart)

Отримуємо всі елементи з класом plus (це кнопки додавання товарів) і зберігаємо їх у змінну buttons.
    
    const buttons = document.querySelectorAll('.plus')

Цей цикл перебирає всі кнопки додавання товарів, щоб додати їм обробники подій.
    
    for (let i = 0; i < buttons.length; i++){
        let button = buttons[i]
    
Цей рядок додає обробник подій для кожної кнопки. Подія click викликає функцію, яка виконується при натисканні на кнопку.
        button.addEventListener(
            type = 'click',
            listener = function(event){
            
 Якщо куки порожні, створюється новий запис у куках з назвою products, де значенням є ID кнопки, яка була натиснута. Збільшується лічильник товарів на 1. Якщо куки вже               існують, додається новий ID до існуючого списку продуктів у куках. Збільшується лічильник товарів на 1. Лічильник товарів відображається у попередньому елементі,                        сусідньому з кнопкою (previousElementSibling).
 
            if (document.cookie == ""){
                document.cookie = `products = ${button.id}; path = /`
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1
            }else{
                let currentProduct = document.cookie.split('=')[1]
                document.cookie = `products = ${currentProduct} ${button.id}; path = /`
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1
                // console.log(button.id.length)
            }
        }
    )
}
#### Файл deleteCookies(cart)
Отримуємо всі кнопки з класом "minus" і зберігаємо їх у змінній listButtonsMinus
    let listButtonsMinus = document.querySelectorAll(".minus")

for (let count = 0; count < listButtonsMinus.length; count++ ){
    let button = listButtonsMinus[count]
    button.addEventListener(
      type = "click",
      listener = (event) =>{
        let cookiesProducts = document.cookie.split('=')[1] 
        let listIdProducts = cookiesProducts.split(" ")

        for (let index = 0; index < listIdProducts.length; index++){
          if (button.id == listIdProducts[index]){
            listIdProducts.splice(index, 1)

            button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1
            break
          }
        }
        
        if (button.nextElementSibling.textContent == 0){
            document.querySelector(`#product-${button.id}`).remove() 
        }
        document.cookie = `products = ${listIdProducts.join(" ")}; path = /`
        
        if (document.cookie.split('=')[1] == ''){
            let h2 = document.createElement('h2') 
            h2.textContent = 'Корзина порожня' 
            document.body.append(h2) 
            document.querySelector('.processing-conteiner').remove()
        }
      }
    )
}
#### Файл Shop
```python
// Вибираємо всі елементи з класом 'button' і зберігаємо їх у listButtons
const listButtons = document.querySelectorAll('.button');

// Вибираємо елемент з класом 'basket-link'
let basketLink = document.querySelector('.basket-link');

// Ініціалізуємо tickCount значенням 0 для відстеження кількості доданих товарів
let tickCount = 0;

// Створюємо новий елемент <p>
let p = document.createElement('p');

// Проходимо через кожну кнопку у listButtons
for (let count = 0; count < listButtons.length; count++) {

    // Отримуємо поточну кнопку в циклі
    let button = listButtons[count];

    // Додаємо обробник події натискання на поточну кнопку
    button.addEventListener(
        'click', // Вказуємо тип події як 'click' (натискання)
        function (event) { // Визначаємо функцію-обробник події
            console.log('додано'); // Виводимо 'додано' в консоль при натисканні на кнопку

            // Створюємо новий елемент <img>
            let img = document.createElement("img");
            // Встановлюємо джерело зображення на 'img/cart-tick.png'
            img.src = 'img/cart-tick.png';
            // Додаємо клас 'cart-tick' до зображення
            img.classList.add('cart-tick');
            // Додаємо зображення до елемента basketLink
            basketLink.appendChild(img);

            // Збільшуємо tickCount на 1
            tickCount++;
            // Встановлюємо текстовий вміст елемента <p> як поточне значення tickCount
            p.textContent = tickCount;
            // Додаємо клас 'cart-p' до елемента <p>
            p.classList.add('cart-p');
            // Додаємо елемент <p> до елемента basketLink
            basketLink.appendChild(p);

            // Якщо кількість товарів більше 9, змінюємо стиль тексту
            if (p.textContent > 9) {
                p.style.fontSize = '10px'; // Змінюємо розмір шрифту
                p.style.paddingTop = '12px'; // Змінюємо відступ зверху
            }

            // Якщо у файлах cookie порожньо, додаємо новий cookie з поточним товаром
            if (document.cookie == '') {
                document.cookie = products=${button.id}; path=/;
            } else { // Інакше оновлюємо існуючий cookie
                let product_id = document.cookie.split('=')[1];
                document.cookie = products=${product_id} ${button.id}; path=/;
            }

            // console.log(button.id.length) // Коментар для виводу довжини id кнопки у консоль
        }
    );
}
// Додатковий код для оновлення відображення корзини

let cookies = document.cookie.split(' ')
// Отримуємо куки і розділяємо їх по пробілах, зберігаємо у змінній cookies

console.log(cookies.length)
// Виводимо в консоль кількість куків

document.querySelector('.final-count-num').textContent = cookies.length
// Оновлюємо текстове вміст елемента з класом "final-count-num" до кількості куків

let count = document.querySelector('.count')
let price = document.querySelectorAll('.price')
// Отримуємо елементи з класами "count" і "price"

if (cookies.length > 1 && cookies.length < 5) {
    document.querySelector('.total-count').textContent = '-товари на суму'
    // Якщо кількість куків більше 1 і менше 5, оновлюємо текстове вміст елемента з класом "total-count"
}

if (cookies.length == 1 ) {
    document.querySelector('.total-count').textContent = '-товар на суму'
    // Якщо кількість куків дорівнює 1, оновлюємо текстове вміст елемента з класом "total-count"
}

let finalCount = document.querySelector(".final-count")
finalCount.textContent = cookies.length * Number(price)
// Оновлюємо текстове вміст елемента з класом "final-count" до загальної кількості куків, помноженої на ціну

document.querySelector('.processing').addEventListener(
    'click', (event) => {
        document.querySelector('.popup-processing').style.display = "flex"
        // Додаємо обробник подій на клік для елемента з класом "processing", який показує спливаюче вікно
    }
)
```
#### Файл Processing
```javaScript
// Розділяємо куки (cookies) на окремі елементи за пробілом
let cookies = document.cookie.split(' ');
console.log(cookies.length); // Виводимо кількість елементів у консоль

// Встановлюємо текстовий вміст елемента з класом 'final-count-num' як кількість куків
document.querySelector('.final-count-num').textContent = cookies.length;

// Знаходимо елемент з класом 'count'
let count = document.querySelector('.count');
// Знаходимо всі елементи з класом 'price'
let price = document.querySelectorAll('.price');

// Якщо кількість куків більша за 1 і менша за 5
if (cookies.length > 1 && cookies.length < 5) {
    document.querySelector('.total-count').textContent = '-товари на суму';
}

// Якщо кількість куків дорівнює 1
if (cookies.length == 1) {
    document.querySelector('.total-count').textContent = '-товар на суму';
}

// Знаходимо елемент з класом 'final-count'
let finalCount = document.querySelector(".final-count");
// Встановлюємо текстовий вміст елемента 'final-count' як добуток кількості куків на ціну
finalCount.textContent = cookies.length * Number(price);

// Додаємо обробник події 'click' на елемент з класом 'processing'
document.querySelector('.processing').addEventListener(
    'click', (event) => {
        // Змінюємо стиль відображення елемента з класом 'popup-processing' на "flex"
        document.querySelector('.popup-processing').style.display = "flex";
    }
);
Пояснення:

Розділяємо рядок куків на окремі елементи за пробілом та виводимо кількість елементів у консоль.
Встановлюємо кількість елементів у куках як текстовий вміст елемента з класом 'final-count-num'.
Знаходимо елементи з класами 'count' та 'price'.
Перевіряємо кількість елементів у куках і відповідно змінюємо текстовий вміст елемента з класом 'total-count'.
Встановлюємо текстовий вміст елемента 'final-count' як добуток кількості куків на ціну.
Додаємо обробник події 'click' на елемент з класом 'processing', який змінює стиль відображення елемента з класом 'popup-processing' на "flex".

```
#### Файл Processing Edit.js
```javascript
// Вибираємо всі елементи з класом 'edit-img-btn' і зберігаємо їх у listButtonImage
let listButtonImage = document.querySelectorAll(".edit-img-btn");

// Проходимо через кожну кнопку у listButtonImage
for (let count = 0; count < listButtonImage.length; count++) {
    let button = listButtonImage[count];
    
    // Додаємо обробник події натискання на поточну кнопку
    button.addEventListener(
        "click", // Вказуємо тип події як 'click'
        (event) => { // Визначаємо функцію-обробник події
            // Відображаємо модальне вікно
            document.querySelector(".modal-window").style.display = "flex";

            // Налаштовуємо властивості інпуту для завантаження зображення
            let inputData = document.querySelector(".input-data");
            inputData.type = "file";
            inputData.accept = "image/*";
            inputData.name = "image";
            // Змінюємо текст мітки в модальному вікні
            document.querySelector(".modal-label").textContent = "CHANGE IMAGE:";
            // Встановлюємо значення кнопки зміни
            document.querySelector('.change-btn').value = image-${button.id};
        }
    );
}

// Вибираємо всі елементи з класом 'edit-name' і зберігаємо їх у listButtonName
let listButtonName = document.querySelectorAll(".edit-name");

// Проходимо через кожну кнопку у listButtonName
for (let count = 0; count < listButtonName.length; count++) {
    let button = listButtonName[count];

    // Додаємо обробник події натискання на поточну кнопку
    button.addEventListener(
        "click", // Вказуємо тип події як 'click'
        (event) => { // Визначаємо функцію-обробник події
            // Відображаємо модальне вікно
            document.querySelector(".modal-window").style.display = "flex";
            
            // Налаштовуємо властивості інпуту для введення тексту
            let inputData = document.querySelector(".input-data");
            inputData.type = "text";
            inputData.name = "name";
            // Змінюємо текст мітки в модальному вікні
            document.querySelector(".modal-label").textContent = "CHANGE TEXT:";
            // Встановлюємо значення кнопки зміни
            document.querySelector('.change-btn').value = name-${button.id};
        }
    );
}

// Вибираємо всі елементи з класом 'edit-price' і зберігаємо їх у listButtonPrice
let listButtonPrice = document.querySelectorAll(".edit-price");

// Проходимо через кожну кнопку у listButtonPrice
for (let count = 0; count < listButtonPrice.length; count++) {
    let button = listButtonPrice[count];

    // Додаємо обробник події натискання на поточну кнопку
    button.addEventListener(
        "click", // Вказуємо тип події як 'click'
        (event) => { // Визначаємо функцію-обробник події
            // Відображаємо модальне вікно
            document.querySelector(".modal-window").style.display = "flex";

            // Налаштовуємо властивості інпуту для введення числа
            let inputData = document.querySelector(".input-data");
            inputData.type = "number";
            inputData.name = "price";
            // Змінюємо текст мітки в модальному вікні
            document.querySelector(".modal-label").textContent = "CHANGE PRICE:";
            // Встановлюємо значення кнопки зміни
            document.querySelector('.change-btn').value = price-${button.id};
        }
    );
}

// Вибираємо всі елементи з класом 'edit-discount' і зберігаємо їх у listButtonDiscount
let listButtonDiscount = document.querySelectorAll(".edit-discount");

// Проходимо через кожну кнопку у listButtonDiscount
for (let count = 0; count < listButtonDiscount.length; count++) {
    let button = listButtonDiscount[count];
// Додаємо обробник події натискання на поточну кнопку
    button.addEventListener(
        "click", // Вказуємо тип події як 'click'
        (event) => { // Визначаємо функцію-обробник події
            // Відображаємо модальне вікно
            document.querySelector(".modal-window").style.display = "flex";

            // Налаштовуємо властивості інпуту для введення числа (знижки)
            let inputData = document.querySelector(".input-data");
            inputData.type = "number";
            inputData.name = "discount";
            // Змінюємо текст мітки в модальному вікні
            document.querySelector(".modal-label").textContent = "CHANGE DISCOUNT:";
            // Встановлюємо значення кнопки зміни
            document.querySelector('.change-btn').value = discount-${button.id};
        }
    );
}

// Додаємо обробник події натискання на елемент з класом 'new-product'
document.querySelector('.new-product').addEventListener(
    'click', (event) => {
        event.preventDefault(); // Відміняємо стандартну поведінку події
        // Відображаємо блок з класом 'new-product-div'
        document.querySelector('.new-product-div').style.display = 'flex';
    }
);
`
```
Пояснення:
1. Для кожного елементу з класом 'edit-img-btn', 'edit-name', 'edit-price', і 'edit-discount' додається обробник події натискання.
2. При натисканні на будь-яку кнопку, відповідно налаштовуються властивості інпуту (тип, прийнятні файли, ім'я).
3. Текст мітки в модальному вікні змінюється відповідно до типу зміни (зображення, текст, ціна, знижка).
4. Для кнопки 'new-product' додається обробник події натискання, який відображає блок для додавання нового продукту.
# Висновки 
- За цей час розробки проекту усі учасники команди навчились головному, як створювати повноцінний веб-додаток. Ми дізнались дуже багато чого нового, наприклад як працювати моделями, що таке Jinja-шаблонізатор, як деплоїти проект на pythonanewhere, як працювати з базою даних через модуль flask_sqlalchemy, що таке міграції та навіщо вони. Навчились автоматично надсилати ел. листи на пошту. Поглибили свої знання у вивченні мови програмування JavaScript. Отже, цей проект дав нам величезні знання, також це чудова нагода попрактикуватись у створення веб-додатків. В майбутньому цей веб-додаток точно дасть початок наступним.
