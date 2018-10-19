First You need to

python3 sales.py(based on the name of the files you created)

Now Curl command
curl -H "Content-Type: application/json" -XPOST "localhost:9200/sales/_doc/_bulk?pretty&refresh" --data-binary "@formatted.json"


You need to change (sales) base on the files you want to run and also you need to change this files(@frommated.json)



In different terminal
Elasticsearch

run
cd elasticsearch-6.4.2
./bin/elasticsearch




Kibana


Open another terminal
run

 cd kibana-6.4.2-darwin-x86_64
 ./bin/kibana
