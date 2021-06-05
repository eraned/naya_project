# **instructions** 

build you image

`$ docker build . -t=elasticsearch-kibana
`

run your container

`$ docker run -d -p 8000:8000 -p 9200:9200 elasticsearch-kibana
`