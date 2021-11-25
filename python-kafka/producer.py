from kafka import KafkaProducer
import json
import time
from datetime import datetime

#producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

sr = open('btc.csv', 'r')
sr.readline()
messages = []
for line in sr:
    data = line.replace('K', '').split(',')
    messages.append({
        'date': datetime.now().isoformat(),
        'price': float(data[1]),
        'volume': float(data[5]) * 1000,
    })
sr.close()
while True:
    #print('begin of file')
    for i in range(len(messages)):
        producer.send('btc', messages[i])
        #print(f'send at: {datetime.now().isoformat()}')
        time.sleep(5)
    #print('end of file')