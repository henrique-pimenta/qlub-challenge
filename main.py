from apiflask import APIFlask
from flask.logging import default_handler
from logger import configure_logger
from views.closest_restaurant_view import views


api = APIFlask(__name__)

api.register_blueprint(views)

api.logger.removeHandler(default_handler)
api.logger.addHandler(configure_logger(log_path='./logs/'))


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)
