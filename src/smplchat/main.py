""" main.py - smplchat """
from ipaddress import IPv4Address

from smplchat.client_list import ClientList
from smplchat.input_utils import prompt_nick
from smplchat.listener import Listener
from smplchat.message_list import MessageList, initial_messages
from smplchat.sender import Sender
from smplchat.tui import UserInterface
from smplchat.message import new_message, MessageType
from smplchat.client_list import ClientList
from smplchat.packet_mangler import unpacker
from .utils import get_my_ip, dprint

def main():
    """ main - the entry point to the application """

    print("Welcome to smplchat!\n")

    self_ip = IPv4Address(get_my_ip())

    dprint(f"INFO: Got ip-address {self_ip}")

    # prompt nickname
    nick = prompt_nick()

    # core

    client_list = ClientList(self_ip) # Initialize ip-list

    listener = Listener()
    msg_list = MessageList()
    initial_messages(msg_list) # adds some helpful messages to the list
    sender = Sender()

    tui = UserInterface(msg_list, nick)

    try:
        while True:

            # Process input form listener
            for rx_msg, remote_ip in listener.get_messages():
                msg = unpacker(rx_msg)
                if msg.msg_type < 128: #relay message
                    if not msg_list.is_seen(msg.uid):
                        sender.send(msg, client_list.get())
                if msg.msg_type == 129: #join reply
                    # TODO: Do the old messages
                    client_list.add_list(msg.ip_addresses)
            client_list.update()
            

            # Process input from UI
            intxt = tui.update(nick)
            if intxt is None:
                pass
            elif intxt.startswith("/quit"):
                msg = new_message(msg_type=MessageType.LEAVE_RELAY, nick=nick,
                        ip=self_ip, msg_list=msg_list)
                #    sender.send(msg)
                #    msg_list.add(msg)
                tui.stop()
                break
            elif intxt.startswith("/nick"):
                nick = intxt.split()[1]
            elif intxt.startswith("/help"):
                initial_messages(msg_list)
            elif intxt.startswith("/join"):
                msg = new_message(msg_type=MessageType.JOIN_REQUEST, nick=nick)
                try:
                    remote_ip = IPv4Address(intxt.split()[1])
                    msg_list.sys_message(f"*** Join request sent to {remote_ip}")
                    sender.send(msg, [remote_ip])
                except:
                    msg_list.sys_message(f"*** Malformed address {intxt.split()[1]}")
            else: # only text to send

                msg = new_message(msg_type=MessageType.CHAT_RELAY, nick=nick,
                        text=intxt, ip=self_ip, msg_list=msg_list)
                msg_list.add(msg)
                sender.send(msg, client_list.get())
    finally:
        # exit cleanup
        listener.stop()
        tui.stop()

if __name__ == "__main__":
    main()
