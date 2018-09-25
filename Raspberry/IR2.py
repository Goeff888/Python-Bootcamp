try:
import pylirc
except ImportError:
raise plugin.MissingDependency(„pylirc“)

import time,os

blocking = 0;

if(pylirc.init(„pylirc“, „/home/pi/Desktop/script/f.conf“, blocking)):

code = {„config“ : „“}
while(code[„config“] != „quit“):

# Very intuitive indeed
if(not blocking):
time.sleep(1)

# Read next code
s = pylirc.nextcode(1)

# Loop as long as there are more on the queue
# (dont want to wait a second if the user pressed many buttons…)
while(s):

# Print all the configs…
for (code) in s:

handle = os.popen(code[„config“])
line = “ “
while line:
line = handle.read()
print line
handle.close()

if(code[„config“] == „blocking“):
blocking = 1
pylirc.blocking(1)

elif(code[„config“] == „nonblocking“):
blocking = 0
pylirc.blocking(0)

# Read next code?
if(not blocking):
s = pylirc.nextcode(1)
else:
s = []

# Clean up lirc
pylirc.exit()

#https://www.marcuslausch.de/2017/08/15/lirc-mit-python-pylirc/