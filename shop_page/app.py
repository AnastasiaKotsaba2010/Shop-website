# Імпортуємо для подальшої роботи модуль flask
import flask

shop_page = flask.Blueprint(
    name = 'shop_page', # назва додатку сторінки 
    import_name= 'shop_page', # назва пакету, у якому створюється змінна (аби в наступних параметрах скоротити шлях)
    template_folder= 'templates', # папка з шаблоном сторінки (абсолютний шлях не варто вказувати через назву пакету)
    static_folder= 'static', # папка зі стилями сторінки
    static_url_path= '/shop_page/' # посилання за яким можна знайти сторінку на веб-сайті
)


