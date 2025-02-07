"""
logging library: Capture logs
"""

print("Configure logger")
print("-"*20)
# -------------

import logging
logging.basicConfig(filename="mylog.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(levelname)s - %(filename)s - %(asctime)s - %(message)s"
                    )

my_logger = logging.getLogger(__name__)

print("Logger configuration is done")

print("#"*40, end="\n\n")
############################


print("Testing my_logger")
print("-"*20)
# -------------

my_logger.info("This is INFO")
my_logger.debug("This is DEBUG")
my_logger.error("This is ERROR")
my_logger.warning("This is WARNING")
my_logger.critical("This is CRITICAL")

print("""
For testing purpose, we wrote some log to mylog.log file, 
Please check
""")

print("#"*40, end="\n\n")
############################
print("using logger in actual program")
print("-"*20)
# -------------

try:
    my_logger.info("Reached try block")
    my_logger.info("Opening file..")
    my_file_handle = open(r"D:\sndkjaj\ashdjsd.txt", "w")
    my_logger.info("Opening file done")
except Exception as e:
    my_logger.info("Reached except block")
    my_logger.error(f"Got Error and Details are: {e}")
    my_logger.info("Reached end of except block")

print("""
logs are captured in mylog.log file, 
Please check
""")

print("#"*40, end="\n\n")
############################