from enum import Enum  # since Python 3.4


class Action(Enum):
    Shutdown = 0
    Reboot = 1
    CloseSession = 2
    Lock = 3
    Suspend = 4
    Hibernate = 5
    Notify = 6
    Execute = 8
    Mail = 9


class Condition(Enum):
    AtTime = 0
    Countdown = 1
    SystemLoad = 2
    Network = 3
    Power = 4
    Drives = 5
