# try_grafana

 - influxdb:1.5.3-alpine
    - [library/influxdb - Docker Hub](https://hub.docker.com/_/influxdb/)

 - grafana/grafana:5.1.4
    - [grafana/grafana - Docker Hub](https://hub.docker.com/r/grafana/grafana/tags/)
    - [Installing using Docker | Grafana Documentation](http://docs.grafana.org/installation/docker/)

## Getting Started

### Influxdb

デフォで豊富なインターフェースを持っている。KVS。時系列に強いとか。

```
docker run --rm -d --name=influxdb -p 8086:8086 say3no/influxdb 
```

admin権限のポートは8083で環境変数がいるよ

```
docker run --rm -d --name=influxdb -e INFLUXDB_ADMIN_ENABLED=true -p 8086:8086 -p 8083:8083 say3no/influxdb -e 
```


```
curl -G http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mydb"
curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'
```





### Grafana

```
docker run --rm -d --name=grafana -p 3000:3000 say3no/grafana -e "GF_SERVER_ROOT_URL=http://grafana.server.name" -e "GF_SECURITY_ADMIN_PASSWORD=secret"
```


## チラシの裏

まーとりあず愚直にチュートリアルやろう。






## Reference

[時系列データベース InfluxDB の基本操作と Grafana 連携を試した - kakakakakku blog](https://kakakakakku.hatenablog.com/entry/2018/03/11/224442)
GUIとかadminでいろいろいじりたいよ〜
