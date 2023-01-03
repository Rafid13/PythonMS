import pika, json

params = pika.URLParameters('amqps://snwftsci:eiBfAIXrTH3uyenftpshNJwhGBFIfDya@rattlesnake.rmq.cloudamqp.com/snwftsci')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties )