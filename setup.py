import argparse
import install
import json

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-H", "--host", required=False, default="localhost",
        help="Hostname of the InfluxDB server (Default: 'localhost')")
    ap.add_argument("-p", "--port", required=False, default=8086, type=int,
        help="Port of the InfluxDB server (Default: 8086)")
    ap.add_argument("-i", "--interval", required=False, default=3600, type=int,
        help="Update Interval in seconds to read data and push to the DB (Default: 3600)")
    ap.add_argument("-d", "--database", required=False, default='iobroker',
        help="Set the default database (Default: 'iobroker')")
    ap.add_argument("-I", "--install", required=False,
        help="Install/Reinstall the geckodriver", action='store_true')
    args = ap.parse_args()

    if args.install:
        install.install()

    config = {
        'host': args.host,
        'port': args.port,
        'database': args.database,
        'interval': args.interval
    }

    configFile = open("config.json", "w")
    json.dump(config, configFile)
    configFile.close()

if __name__ == '__main__':
    main()