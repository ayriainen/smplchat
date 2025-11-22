""" main.py - smplchat """
from smplchat.input_utils import prompt_nick, prompt_self_addr
from smplchat.listener import Listener
from smplchat.message_list import MessageList, initial_messages
from smplchat.packet_mangler import ChatRelayMessage
from smplchat.dispatcher import Dispatcher
from smplchat.tui import UserInterface
from .utils import generate_uid, get_time_from_uid

def new_message(nick, text, ip, msg_list):
    """ Generates new message. TODO: move this in better place """
    uid = generate_uid()
    return ChatRelayMessage(
        msg_type = 0,
        uniq_msg_id = uid,
        sender_ip = ip,
        sender_local_time = get_time_from_uid(uid),
        old_message_ids = [], #msg_list.get_latest_uids(),
        sender_nick = nick,
        msg_text = text)

def main():
    """ main - the entry point to the application """

    print("Welcome to smplchat!")

    # prompt nickname
    nick = prompt_nick()

    # prompt address or use default
    self_addr = prompt_self_addr()

    # core
    listener = Listener(port=self_addr[1])
    msg_list = MessageList()
    initial_messages(msg_list) # adds some helpful messages to the list
    dispatcher = Dispatcher(
        listener=listener,
        message_list=msg_list,
        nick=nick,
        self_addr=self_addr
    )

    tui = UserInterface(msg_list, nick)

    while (True):
        #for rx_msg in listener.update():
        #    msg = unpacker(rx_msg)
        #    if msg.type < 128: #relay message
        #	if msg_list.is_seen:
        #          dispatcher.send(message)
        intxt = tui.update()
        if intxt == None:
            continue
        if intxt.startswith("/nick"):
            nick = intxt.split()[1]
            continue
        if intxt.startswith("/quit"):
        #    msg = LeaveRelayMessage(...)
        #    dispatcher.send(msg)
        #    msg_list.add(msg)
            tui.stop()
            break
        
        msg = new_message(nick, intxt, self_addr, msg_list)
        msg_list.add(msg)
        #dispatcher.send(msg)


    #try:
        # curses
        #run_tui(msg_list, dispatcher, nick)
        pass # remove once tui done
    #finally:
        # exit cleanup
    dispatcher.stop()
    listener.stop()
    tui.stop()

if __name__ == "__main__":
    main()
