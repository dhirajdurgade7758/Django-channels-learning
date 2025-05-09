from channels.consumer import SyncConsumer, AsyncConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("WebSocket connected")
        self.send({
            "type": "websocket.accept"
        })

    # def websocket_receive(self, event):
    #     print("WebSocket message received:", event['text'])
    #     for i in range(50):
    #         self.send({
    #             "type": "websocket.send",
    #             # "text": f"You said: {event['text']}"
    #             "text":str(i),
    #         }) 
    #         sleep(1)
            
    def websocket_receive(self, event):
        print("WebSocket message received:", event['text'])
        for i in range(50):
            self.send({
                "type": "websocket.send",
                # "text": f"You said: {event['text']}"
                "text":json.dumps({"count": str(i)}),
            }) 
            sleep(1)
   

    def websocket_disconnect(self, event):
        print("WebSocket disconnected") 


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("WebSocket connected") 
        await self.send({
            "type": "websocket.accept"
        })


    async def websocket_receive(self, event):
        print("WebSocket message received")
        await self.send({  
            "type": "websocket.send",
            "text": f"You said: {event['text']}"
            # "text": str(event['text']),
        })
        for i in range(50):
            await self.send({
                "type": "websocket.send",
                # "text": f"You said: {event['text']}"
                "text":str(i),
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("WebSocket disconnected") 
    


        # Perform synchronous operations here       

