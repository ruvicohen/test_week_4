from flask import Flask
from repository.database import drop_tables
from service.seed import seed

app = Flask(__name__)

if __name__ == "__main__":
    drop_tables()
    seed()
    # app.register_blueprint(user_blueprint, url_prefix="/api/user")
    # app.register_blueprint(store_blueprint, url_prefix="/api/store")
    # app.register_blueprint(movie_blueprint, url_prefix="/api/movie")
    # app.register_blueprint(subscription_blueprint, url_prefix="/api/subscription")
    # app.register_blueprint(rental_blueprint, url_prefix="/api/rental")
    app.run(debug=True)