# backend/mesh_app/comm.py
import os
import base64
import json
from django.conf import settings
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from hashlib import sha256

# ---------------------------
# Key derivation (demo-friendly)
# ---------------------------
def _get_shared_key():
    """
    Derive a 32-byte key from Django SECRET_KEY (demo purposes).
    If you want a custom key, set MESH_SHARED_KEY in settings.py as a base64 string.
    """
    # If project provided an explicit key in settings, use it
    mesh_key_b64 = getattr(settings, "MESH_SHARED_KEY_B64", None)
    if mesh_key_b64:
        try:
            return base64.b64decode(mesh_key_b64)
        except Exception:
            pass

    # Otherwise derive from SECRET_KEY (deterministic, demo-friendly)
    secret = getattr(settings, "SECRET_KEY", "default-demo-secret").encode()
    # SHA-256 -> 32 bytes, suitable for AES-256
    return sha256(secret).digest()

# ---------------------------
# AES-GCM helpers
# ---------------------------
def encrypt_message(plaintext: str) -> str:
    """
    Encrypt plaintext (str) and return a base64-packed JSON string:
    base64( json.dumps({"nonce": b64, "ct": b64}) )
    """
    key = _get_shared_key()
    aesgcm = AESGCM(key)
    # 12-byte nonce recommended for AES-GCM
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, plaintext.encode(), associated_data=None)

    payload = {
        "nonce": base64.b64encode(nonce).decode(),
        "ct": base64.b64encode(ct).decode(),
    }
    packed = base64.b64encode(json.dumps(payload).encode()).decode()
    return packed

def decrypt_message(packed_b64: str) -> str:
    """
    Accept the base64-packed JSON string produced by encrypt_message and return plaintext.
    Raises exceptions on failure (bad key / tamper).
    """
    key = _get_shared_key()
    aesgcm = AESGCM(key)

    # unpack
    try:
        decoded = base64.b64decode(packed_b64.encode())
        payload = json.loads(decoded.decode())
        nonce = base64.b64decode(payload["nonce"])
        ct = base64.b64decode(payload["ct"])
        plaintext = aesgcm.decrypt(nonce, ct, associated_data=None)
        return plaintext.decode()
    except Exception as e:
        # For demo clarity, re-raise or return a sentinel
        raise ValueError(f"Decryption failed: {e}")

# ---------------------------
# In-memory "network" simulation helpers (existing demo behavior)
# ---------------------------
_messages = []

def broadcast_message(packed_message: str):
    """
    Simulate broadcasting an encrypted message bytes/string to the local mesh.
    For a real LAN, you'd send bytes over UDP/TCP; for the demo we store strings.
    """
    global _messages
    _messages.append(packed_message)

def get_messages():
    """
    Retrieve all messages and clear the network buffer (simulate delivery).
    Returns a list of packed base64 strings.
    """
    global _messages
    msgs = _messages.copy()
    _messages.clear()
    return msgs
