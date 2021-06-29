
import logging
import logging.handlers
import os

def testfunc():
 msg1 = "got"
 msg2 = "here"
 print(msg1)
 logging.info(msg1)
 print(msg2)
 logging.warning(msg2)


handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "LogFile.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
logging.basicConfig(level=logging.INFO)
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)
testfunc()

try:
 raise Exception
except Exception:
 logging.exception("Exception in main(): ")


a = 'b'
b = 0
try:
 c = a / b
except Exception as e:
 logging.exception("Exception occurred")

a = 5
b = 0
try:
 c = a / b
except Exception as e:
 logging.exception("Exception occurred")




