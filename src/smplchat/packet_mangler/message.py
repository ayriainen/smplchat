""" smplchat.message - message dataclasses are defined here """
from dataclasses import dataclass

@dataclass
class Message:
    """ message - basis for every type of message """
    msg_type: int

@dataclass
class RelayMessage(Message):
    """ relay message - messages that are distributed as is in the system """
    uniq_msg_id: int
    sender_ip: int
    sender_local_time: int
    old_message_ids: [int]
    sender_nick: str

@dataclass
class ChatRelayMessage(RelayMessage):
    """ chat relay message - actual messages send by users """
    msg_text: str

@dataclass
class JoinRelayMessage(RelayMessage):
    """ join relay message - the message formed by client that handles join request """

@dataclass
class LeaveRelayMessage(RelayMessage):
    """ leave relay message - send by client leaving the chat """

@dataclass
class KeepaliveRelayMessage(Message):
    """ keepalive relay message - time to time relay message to be distributed for
                                  other clients not to consider client disconnected.
    """
    uniq_msg_id: int
    sender_ip: int
