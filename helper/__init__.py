import os, platform
from .log import Logger

def clear_logs():
    os.system('clear' if platform.system() == 'Linux' else 'cls')
