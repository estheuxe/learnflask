from flask import Flask
from config import Configuration

from posts.blueprint import posts

# для доступа к фласку
app = Flask(__name__)
# привязываем класс конфигурации
app.config.from_object(Configuration)
# регистрация блюпринта
app.register_blueprint(posts, url_prefix='/blog')