"""Prime Anagram using Queue Program

This program is used to find prime anagram within 0  to 1000 range and print through queue

Author:
    Saurabh <singh.saurabh3333@gmail.com>

Since:
    20 Nov,2018
"""

from com.bridgelabz.util.datastructure_util import *


def anagram_runner():
    """
    This method act as runner for anagram_queue() method.
    :return: nothing
    """
    logic_obj = Logic()
    logic_obj.anagram_queue()


if __name__ == "__main__":
    anagram_runner()
