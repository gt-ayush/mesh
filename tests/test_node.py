import pytest
from mesh_app.routing import send_message, receive_messages

def test_send_and_receive():
    # Send a message
    test_msg = "Hello Test Node"
    send_message(test_msg)

    # Receive all pending messages
    messages = receive_messages()

    assert isinstance(messages, list)
    assert test_msg in messages
