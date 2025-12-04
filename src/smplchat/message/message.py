""" smplchat.message - message dataclasses are defined here """
from dataclasses import dataclass
from enum import IntEnum
from ipaddress import IPv4Address

class MessageType(IntEnum):
    """ Different types of allowed message types and corresponding int """
    CHAT_RELAY = 0
    JOIN_RELAY = 1
    LEAVE_RELAY = 2
    KEEPALIVE_RELAY = 3
    JOIN_REQUEST = 128
    JOIN_REPLY = 129
    OLD_REQUEST = 130
    OLD_REPLY = 131

@dataclass
class Message:
    """ message - basis for every type of message """

@dataclass
class ChatRelayMessage(Message):
    """ chat relay message - actual messages send by users """
    uniq_msg_id: int
    sender_ip: IPv4Address
    old_message_ids: list[int]
    sender_nick: str
    msg_text: str

@dataclass
class JoinRelayMessage(Message):
    """ join relay message - the message formed by client that handles join request """
    uniq_msg_id: int
    sender_ip: IPv4Address
    old_message_ids: list[int]
    sender_nick: str

@dataclass
class LeaveRelayMessage(Message):
    """ leave relay message - send by client leaving the chat """
    uniq_msg_id: int
    sender_ip: IPv4Address
    old_message_ids: list[int]
    sender_nick: str

@dataclass
class KeepaliveRelayMessage(Message):
    """ keepalive relay message - time to time relay message to be distributed for
                                  other clients not to consider client disconnected.
    """
    uniq_msg_id: int
    sender_ip: IPv4Address

@dataclass
class JoinRequestMessage(Message):
    """ join request message - the first message client sends to join the chat """
    uniq_msg_id: int
    sender_nick: str

@dataclass
class JoinReplyMessage(Message):
    """ join reply message - informs newly joined client about history and ip:s"""
    old_message_ids: list[int]
    ip_addresses: list[IPv4Address]

@dataclass
class OldRequestMessage(Message):
    """ old request message - message to request message by id """
    uniq_msg_id: int

@dataclass
class OldReplyMessage(Message):
    """ old reply message - reply for old message request """
    old_msg_type: int
    uniq_msg_id: int
    sender_nick: str
    msg_text: str

def is_relay_message(msg: Message):
    """ helper to figure out if message is relay type """
    return isinstance( msg, (
        ChatRelayMessage,
        JoinRelayMessage,
        LeaveRelayMessage,
        KeepaliveRelayMessage) )