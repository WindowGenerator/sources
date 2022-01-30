import json
import random
import string
from typing import Dict, Iterator, List

strings = string.ascii_letters + string.digits


def generate(ids_ranges: List[Iterator[int]]) -> List[Dict]:
    out = []
    for _range in ids_ranges:
        for _id in _range:
            out.append({"id": _id, "name": ''.join(random.sample(strings, 10))})

    return out


def main() -> None:
    informnation = [
        {
            'name': 'source_1.json',
            'data': [range(1, 11), range(31, 41)],
        },
        {
            'name': 'source_2.json',
            'data': [range(11, 21), range(41, 51)],
        },
        {
            'name': 'source_3.json',
            'data': [range(21, 31), range(51, 61)],
        },
    ]
    for elem in informnation:

        with open(elem['name'], 'wt') as file_fd:
            data = generate(elem['data'])
            file_fd.write(json.dumps(data))


if __name__ == '__main__':
    main()
