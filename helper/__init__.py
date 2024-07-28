import os, platform


def clear_logs():
    os.system('clear' if platform.system() == 'Linux' else 'cls')
