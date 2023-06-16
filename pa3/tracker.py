'''
An application that tracks finances with persistence with through the utilization of a SQL database.

Author: Brandon J. Lacy (AG3NTZ3R0)
'''
import sys

from functools import partial
from transaction import Transaction


# Author: Brandon J. Lacy (AG3NTZ3R0)
# Store the arguments from the command line execution of the script
ARG = ""
vals = ()
# No arguments so prompt the user for them
if len(sys.argv) == 1:
    ARG = input('cmd > ').split(' ')
else:
    ARG = sys.argv[1]
    # Store the values for the option
    vals = tuple(val for val in sys.argv[2:])

# Author: Brandon J. Lacy (AG3NTZ3R0), Eric Wang, Grace Hu
trans_orm = Transaction('tracker.db')
# Act upon the option specified by the user (TEAM: REPLACE "" WITH METHOD AS SEEN BELOW)
options = {
    '--help': "",
    '--quit': "",
    '--show-cat': "",
    '--add-cat': partial(trans_orm.add_category),
    '--mod-cat': partial(trans_orm.modify_category),
    '--show-trans': partial(trans_orm.select_all),
    '--add-trans': partial(trans_orm.add),
    '--del-trans': partial(trans_orm.delete),
    '--sum-trans-d': partial(trans_orm.sum_date),
    '--sum-trans-m': partial(trans_orm.sum_month),
    '--sum-trans-y': partial(trans_orm.sum_year),
    '--sum-trans-c': partial(trans_orm.sum_category),
    '--print-menu': "",
}

# Author: Brandon J. Lacy (AG3NTZ3R0)
try:
    result = options[ARG](vals)
    if len(result) > 0:
        for i in result:
            print(i)
    else:
        print("Completed.")
except IndexError:
    print("There were less parameters than expected.")
except KeyError:
    print("Unavailable option specified.")
