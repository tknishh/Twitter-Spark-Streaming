import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import Stream
import socket
import json

# Set up Your Credentials
consumer_keys = "ZCSFj2T9NPYDKAOfm8DfwqlWC"
consumer_secrets = "bDdFPxVz6Lzl358yLc5jDgqoTRpxl6zEHqxt67sxGtkdeFMpGR"
access_token = "936311765872152577-HgZn02ZxXRiaMbMyjKDvUaPQVdeLCO3"
access_secrets = "GVnzbceDJ8ggmV6mId5MQgHdreIeucNThIZOnQ7xUr6Rg"

class TweetsListener(Stream):
    
    def __init__(self, *args, csocket):
        super().__init__(*args)
        self.client_socket = csocket
        
    def om_data(self,data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode("utf-8"))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True
    
def sendData(c_socket):
    twtr_stream = TweetsListener(
        consumer_keys, consumer_secrets,
        access_token, access_secrets,
        csocket=c_socket
    )
    twtr_stream.filter(track=['bgmi'])
        
if __name__ == "__main__":
    s = socket.socket()        # Create a socket Object
    host = "127.0.0.1"         # get local machine name
    port = 5554                # Reserve a port for your service
    s.bind((host, port))       # Bind to the port
    
    print("Listening on port: %s" % str(port))
    
    s.listen(5)                # Wait for client connection
    c, addr = s.accept()       # Establish connection with client
    
    print("Received request from: " + str(addr))
    
    sendData(c)