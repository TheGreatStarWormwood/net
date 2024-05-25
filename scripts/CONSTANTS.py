from enum import Enum

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       DO NOT TOUCH
#
#       use these and
#       dont add more
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class MessageType(Enum):
    COMMAND = "command"
    MESSAGE = "message"
    ACK = "ack"
    NACK = "nack"
    RESP = "resp"
    INFO = "info"