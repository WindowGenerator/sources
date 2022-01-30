import json
import time
from typing import Dict, List

from flask import Flask, request

from transmitters.parser import DATA_PATH, PORT

application = Flask(__name__)


def get_data() -> List[Dict]:
    with open(DATA_PATH, 'rt') as file_fd:
        return json.loads(file_fd.read())


def get_sleep_seconds(request) -> int:
    sleep = int(request.args['sleep'])
    return sleep / 1000.0


@application.route('/')
def call():
    time.sleep(get_sleep_seconds(request))
    return dict(data=get_data())


if __name__ == '__main__':
    application.run(debug=True, port=PORT)
