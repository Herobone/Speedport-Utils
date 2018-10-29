import argparse
import install
import json

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-H", "--host", required=False, default="localhost",
        help="Hostname of the InfluxDB server (Default: 'localhost')")
    ap.add_argument("-p", "--port", required=False, default=8086,
        help="Port of the InfluxDB server (Default: 8086)")
    ap.add_argument("-i", "--interval", required=False, default=3600,
        help="Update Interval in seconds to read data and push to the DB (Default: 3600)")
    ap.add_argument("-d", "--database", required=False, default='iobroker',
        help="Set the default database (Default: 'iobroker.global')")
    ap.add_argument("-I", "--install", required=False, default='n',
        help="Install/Reinstall the geckodriver (Default: 'n')")
    args = vars(ap.parse_args())

    if args["install"] is 'y':
        install.install()

    config = {
        'host': args["host"],
        'port': args["port"],
        'database': args["database"],
        'interval': int(args["interval"])
    }

    configFile = open("config.json", "w")
    json.dump(config, configFile)
    configFile.close()

if __name__ == '__main__':
    main()