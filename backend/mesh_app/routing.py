import threading
from .comm import broadcast_message, get_messages
from hashlib import sha256

# Simple in-memory message queue
_message_queue = []

def generate_key():
    """Generate a simple key (can be extended to timestamp + random)"""
    return sha256(b"mesh_secret").digest()

def encrypt_message(msg):
    key = generate_key()
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(msg.encode())])

def decrypt_message(enc_msg):
    key = generate_key()
    return "".join([chr(b ^ key[i % len(key)]) for i, b in enumerate(enc_msg)])

def send_message(msg):
    """Encrypt and broadcast message"""
    enc = encrypt_message(msg)
    broadcast_message(enc)
    _message_queue.append(enc)

def receive_messages():
    """Decrypt messages from queue and any new ones"""
    new_msgs = get_messages()
    for msg in new_msgs:
        _message_queue.append(msg)
    return [decrypt_message(m) for m in _message_queue]
