from flask import Flask
from router.router import router
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(base_dir, 'models', 'templates')
print(f"Diretório atual: {templates_path}")

app = Flask(__name__, template_folder=templates_path)

app.register_blueprint(router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)