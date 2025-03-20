from flask import Flask
from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliiteCOnnectionHandle
from src.main.routes.products_routes import producs_routes_bp

redis_connection_handle = RedisConnectionHandler()
sqlite_connection_handle = SqliiteCOnnectionHandle()

redis_connection_handle.connect()
sqlite_connection_handle.connect()

app = Flask(__name__)

app.register_blueprint(producs_routes_bp)
