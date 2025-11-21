"""argparsing helper, could be in some misc or utils folder too"""
import argparse
from smplchat import settings

def parse_host_port(s):
    """Parse host:port or host."""
    if ":" in s:
        host, port_s = s.rsplit(":", 1)
        return host, int(port_s)
    return s, settings.PORT

def parse_partners(partners_str):
    """Parse list of host ports, using parse_host_port."""
    peers = []
    if not partners_str:
        return peers

    for item in partners_str.split(","):
        item = item.strip()
        if not item:
            continue
        peers.append(parse_host_port(item))

    return peers

def parse_args():
    """Parses arguments/commands."""
    parser = argparse.ArgumentParser(description="smplchat")

    parser.add_argument(
        "--self",
        dest="self_addr",
        help="your ip and port with : inbetween like host:post",
        required=False,
    )

    parser.add_argument(
        "--partners",
        default="",
        help="list of host:port separated by comma",
    )

    parser.add_argument(
        "--nick",
        "--author",
        dest="nick",
        default="anon",
        help="nickname for chat",
    )

    return parser.parse_args()
