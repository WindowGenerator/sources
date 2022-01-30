import asyncio
import threading
from functools import partial
from typing import Dict, List

import requests
from flask import Flask, g

application = Flask(__name__)


reqs = [
    'http://localhost:8091?sleep=1000',
    'http://localhost:8092?sleep=5000',
    'http://localhost:8093?sleep=1000',
]


@application.before_request
def init_loop():
    try:
        g.loop = asyncio.get_event_loop()
        print('got event loop for', threading.current_thread().name)
    except RuntimeError:
        g.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(g.loop)
        print('created new event loop for', threading.current_thread().name)


async def _gather_requests():
    responses = await asyncio.gather(
        *[_call_request(url) for url in reqs], return_exceptions=True
    )

    full_data = list()

    for response in responses:
        if isinstance(response, Exception):
            continue

        data = response.json()
        full_data.extend(data['data'])

    return sorted(full_data, key=lambda item: item['id'])


@application.route('/gather', methods=['GET'])
def gather():
    return {
        "data": g.loop.run_until_complete(_gather_requests()),
    }


async def _call_request(url: str, timeout: int = 50) -> List[Dict]:
    return await g.loop.run_in_executor(
        None, partial(requests.get, url, timeout=2, params=dict(sleep=timeout))
    )


if __name__ == '__main__':
    application.run(debug=True, port=9090)
