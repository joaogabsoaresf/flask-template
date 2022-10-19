from __init__ import app
import os
from dotenv import load_dotenv
load_dotenv()
env = os.getenv("ENV")


@app.route('/', methods=['GET'])
def index():
    return "Online!!!"


if env == 'LOCAL':
    app.run(host='0.0.0.0', port = '5000')

elif env == 'Production':
    if __name__=='main':
        port = int(os.getenv('PORT'), '5000')
        app.run(host='0.0.0.0', port = port)