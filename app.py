from flask import Flask

from controller.target_controller import target_blueprint
from repository.database import drop_tables
from service.seed import seed

app = Flask(__name__)

if __name__ == "__main__":
    seed()
    app.register_blueprint(target_blueprint, url_prefix="/api/target")
    app.run(debug=True)