""" smplchat.settings - Contains global settings like default ports """
from os import getenv
from sys import stderr
from ipaddress import IPv4Address


ENV_PREFIX="SMPLCHAT_"
def env_or_default(var, default_value, conversion_function):
    """ Tries to read enviroment varable, but if not valid or not there uses default"""
    if var not in globals():
        try:
            env_value = getenv(ENV_PREFIX+var)
            if not env_value:
                return default_value
            return conversion_function(env_value)
        except ValueError:
            print(f"Ignoring invalid {ENV_PREFIX+var} environmental variable",
                file=stderr)
            return default_value
    return globals()[var]

# adjust these constants to your liking to change system behavior

# how many random peers gossipped to
GOSSIP_FANOUT = env_or_default("GOSSIP_FANOUT", 2, int)

# seen limit for a chat/join/leave/keepalive relay
RELAY_SEEN_LIMIT = env_or_default("RELAY_SEEN_LIMIT", 2, int)

# After 300s we can assume connection is lost
NODE_TIMEOUT = env_or_default("NODE_TIMEOUT", 300, int)

# keepalive's interval in seconds
KEEPALIVE_INTERVAL = env_or_default("KEEPALIVE_INTERVAL", 2, int)

# how often list cleanup (msg, keepalive, client) occurs in seconds
CLEANUP_INTERVAL = env_or_default("CLEANUP_INTERVAL", 60, int)

# latest msgs spread with relays, note: JOIN_REPLY is multiplier of this
LATEST_LIMIT = env_or_default("LATEST_LIMIT", 50, int)

# max number of messages in history, trimmed every CLEANUP_INTERVAL timer
MAX_MESSAGES = env_or_default("MAX_MESSAGES", 2000, int)

# set to something to print out DEBUG information to stderr
DEBUG = env_or_default("DEBUG", None, str)

# adjust listener port
PORT = env_or_default("PORT", 62733, int)

# testing option to adjust how many percent of dispached packets to be dropped
DROP_PERCENT = env_or_default("DROP_PERCENT", 0, int)

# Sets nick beforehand
NICK = env_or_default("NICK", None, str)

# Gives join command as first action when app is up and running
JOIN = env_or_default("JOIN", None, IPv4Address)
