# vim: set fileencoding=utf-8 :
import commands
import StringIO
import datetime
from influxdb import InfluxDBClient

client = InfluxDBClient(host='172.50.1.3', port='8086', username='root', password='root')
DBNAME_CPUS = 'sar_cpus'


def main():
    client.create_database(DBNAME_CPUS)
    insert_sar_cpus()


def insert_sar_cpus():
    exit_status, stdout = commands.getstatusoutput('sar -P ALL 1 1')  # cpu
    stdout = StringIO.StringIO(stdout)
    lines = stdout.readlines()[2::]  # 不要なヘッダである頭２行はけす
    for line in lines:
        splited = line.split()
        if (len(splited) is not 0) and not (splited[1] == 'CPU'):
            client.write_points(format_data(splited), database=DBNAME_CPUS, time_precision='s')


def format_data(data):
    json_body = [
        {
            "time": datetime.datetime.now().isoformat(),
            "measurement": "cpus",
            "tags": {
                "cpu": data[1]
            },
            "fields": {
                "user": data[2],
                "nice": data[3],
                "system": data[4],
                "iowait": data[5],
                "steal": data[6],
                "idle": data[7]
            }
        }
    ]

    return json_body


if __name__ == '__main__':
    main()
