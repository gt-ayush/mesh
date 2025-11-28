
# Simple LAN message simulation (can be extended with sockets or WebSockets)

_messages = []

def broadcast_message(msg_bytes):
    """Simulate sending message to network"""
    global _messages
    _messages.append(msg_bytes)

def get_messages():
    """Return all messages sent in the network"""
    global _messages
    msgs = _messages.copy()
    _messages.clear()  # simulate delivery
    return msgs
