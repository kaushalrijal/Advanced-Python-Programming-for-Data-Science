# import pdb



# aList = [1, 2, 3, 4, 5]


# pdb.set_trace()
# while (True):
#     aList.pop()

# import pdb

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f = f*1
#         return f

# pdb.set_trace()

# fact(5)


#logging

import logging


logging.basicConfig(level=logging.INFO, filename="Day5.log", filemode="a")

logging.info("THIS IS A INFO")
logging.debug("THIS IS A DEBUG")
logging.warning("THIS IS A WARNING")
logging.error("THIS IS A ERROR")
logging.critical("DANGER!!!!")

