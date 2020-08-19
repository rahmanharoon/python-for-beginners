import time
from imp import reload
import module1
time.sleep(30)
reload(module1)
time.sleep(30)
reload(module1)
print("This is test file")
