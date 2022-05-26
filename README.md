# SmartMonitor
Hydroponic Cultivation Monitoring System

[Capstone Project](https://wiki.sj.ifsc.edu.br/index.php/Sistema_de_Monitoramento_de_cultivo_hidrop%C3%B4nico)

Telecommunications Engineering - IFSC/SJ

* Hardware: ESP2866 Lolin
* Sensors: DHT22, BH1750, DS1822 e Guva-S12SD
* Language: Micropython


# For docker
After installing [docker](https://docs.docker.com/get-docker/) you must create a folder called volumes and inside it the folders node red data, influxdb and grafana. Then run the command below in the terminal to upload the containers.

* `docker-compose up -d`

