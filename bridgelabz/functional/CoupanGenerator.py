"""Coupon code generation program

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

Author:
    Saurabh <saurabh.singh@gmail.com>

Since:
    19th Nov, 2018

"""

# Utility import
from com.bridgelabz.util.utility import Utility


def runCoupon():
    """Connects to the next_node available port.

    Args:
    Raises:
      ValueError: If the minimum port specified is less than 1024.
      ConnectionError: If no available port is found.
    Returns:
      The new minimum port.
    """
    try:
        utility_obj = Utility()
        print("Enter Number of Coupans you want")
        no_of_coupans=utility_obj.get_int()
        random_number_count, store_coupans = utility_obj.coupan_generator(no_of_coupans)
        print("Number of Random Number Needed to Generate given number of coupans =>"+str(random_number_count))
        print("The Distinct Coupans are as follows")
        for i in store_coupans:
            print(i)
    except:
        print("error")



if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    runCoupon()

