import pytest
from mesh_app.comm import broadcast_message, inbox

def test_broadcast_message():
    message = "Test broadcast"
    broadcast_message(message)

    # Inbox should contain the message
    assert message in inbox
