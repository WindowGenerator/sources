import argparse
import os


def parse():
    parser = argparse.ArgumentParser(description="Transmitter settings")
    parser.add_argument("-f", "--data-path", dest="data_path", required=True)
    parser.add_argument("-p", "--port", type=int, required=True)

    return parser.parse_args()


args = parse()


DATA_PATH = os.path.join("transmitters/data", args.data_path)
PORT = args.port
