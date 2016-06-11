import yweather
client = yweather.Client()
print client.fetch_woeid('Albania')
