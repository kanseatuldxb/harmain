# smartlift/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LiftLogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("lift_logs", self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({"status": "connected"}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("lift_logs", self.channel_name)

    async def receive(self, text_data):
        # optional echo or control handler
        await self.send(text_data=json.dumps({"echo": text_data}))

    async def send_lift_log(self, event):
        await self.send(text_data=json.dumps(event["data"]))
