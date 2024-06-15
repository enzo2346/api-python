from flask import Flask
import yaml

app = Flask(__name__)

with open("src/config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=cfg['DEBUG'], host=cfg['HOST'], port=cfg['PORT'])