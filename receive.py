from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-ca28baa7-6cad-4d4a-be94-c5c734a2a66a", subscribe_key="sub-c-cbcf32a6-1f74-11e7-bd07-02ee2ddab7fe")

def callback(message, channel):
    print(message)
  
  
def error(message):
    print("ERROR : " + str(message))

pubnub.subscribe(channels='my_channel', callback=callback, error=error)


