# backend/mesh_app/routing.py
from .comm import broadcast_message, get_messages, encrypt_message, decrypt_message

# Simple in-memory message store for local node
_node_store = []

def send_message(msg: str):
    """
    Encrypt the message and broadcast it to the simulated mesh.
    Also keep a local copy of the encrypted payload (optional).
    """
    packed = encrypt_message(msg)  # base64-packed JSON string
    broadcast_message(packed)
    # store encrypted for local history if you want
    _node_store.append(packed)
    return packed

def receive_messages():
    """
    Pull any new messages from the network, decrypt them and return plaintext list.
    Decrypted messages are appended to local store for demo visibility.
    """
    decrypted = []
    # get messages broadcasted by anyone
    new_msgs = get_messages()
    for packed in new_msgs:
        try:
            pt = decrypt_message(packed)
        except Exception as e:
            pt = f"[DECRYPTION_ERROR: {e}]"
        decrypted.append(pt)
        # maintain local store (encrypted) if desired
        _node_store.append(packed)

    # Also decrypt any previously stored messages (so frontend shows whole history)
    # For simplicity, decrypt everything in _node_store (could duplicate)
    full_plain = []
    for p in _node_store:
        try:
            full_plain.append(decrypt_message(p))
        except Exception:
            full_plain.append("[DECRYPTION_ERROR]")

    # Avoid duplicates in returned list: return full_plain (demo-friendly)
    return full_plain
