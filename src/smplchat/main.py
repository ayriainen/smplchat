""" main.py - smplchat """
from smplchat.input_utils import prompt_nick, prompt_self_addr
from smplchat.listener import Listener
from smplchat.message_list import MessageList, initial_messages
from smplchat.dispatcher import Dispatcher
#from smplchat.tui import run_tui

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
    
    while (True):
        #listener.update()
        #rx_msgs = listener.get()
        #for rx_msg in rx_msgs:
        #    msg = unpacker(rx_msg)
        #    if msg.type < 128: #relay message
        #	if msg_list.
        #intxt = tui.update
        #if intxt.startswith("/quit"):
        #    msg = LeaveRealyMessage(...)
        #    dispatcher.send(msg)
        #    msg_list.add(msg)
        #    break
        #elif intxt.startswith("/nick"):
        #    nick = intxt.split()[1]
        #else:
        #    msg = ChatRelayMessage(...)
        #    dispatcher.send(msg)
        #    msg_list.add(msg)
        #...
        break


    try:
        # curses
        #run_tui(msg_list, dispatcher, nick)
        pass # remove once tui done
    finally:
        # exit cleanup
        dispatcher.stop()
        listener.stop()

if __name__ == "__main__":
    main()
