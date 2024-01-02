import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class NotificationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        await self.accept()

        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!',
        }))
        
        

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        await self.send(text_data= json.dumps({
            'message': message
        }))

    async def send_notification(self, msg):
        message = msg['message']
        topic = msg['topic']
        body = msg['body']

        print("THIS IS CONSUMER -->", message)

        await self.send(text_data=json.dumps({
            'message': message,
            'topic': topic,
            'body': body,
        }))

    async def other(self):
        await self.send("Hello from the other side!")

@sync_to_async
def mark_notification_as_seen(notificaiton_id):
    pass