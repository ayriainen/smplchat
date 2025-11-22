""" smplchat.message_gen - functions to generate messages """
from smplchat.packet_mangler import ChatRelayMessage
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
