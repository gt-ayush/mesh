# backend/mesh_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .routing import send_message, receive_messages

class ChatConsumer(AsyncWebsocketConsumer):
    group_name = "mesh_group"

    async def connect(self):
        # Accept connection and add to group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Optionally send existing history on connect
        history = receive_messages()  # returns plaintext list
        await self.send(text_data=json.dumps({"type": "history", "messages": history}))

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        """
        Receive JSON messages from WebSocket client.
        Expected format: {"type":"chat","message":"hello"}
        """
        if text_data is None:
            return

        try:
            payload = json.loads(text_data)
        except Exception:
            return

        msg_type = payload.get("type")
        if msg_type == "chat":
            msg = payload.get("message", "")
            if not msg:
                return

            # Persist / encrypt / broadcast via your existing routing (server-side)
            send_message(msg)  # encrypts and stores in network simulation

            # Broadcast plaintext to all connected WebSocket clients in the group
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "chat.message",  # triggers chat_message below
                    "message": msg,
                }
            )

    async def chat_message(self, event):
        """Handler to forward chat messages to WebSocket clients."""
        msg = event.get("message")
        await self.send(text_data=json.dumps({"type": "chat", "message": msg}))
