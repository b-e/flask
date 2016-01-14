from yowsup.demos import echoclient

import sys

credentials = ("393495538473", "WVNyjWfQgY3W1ZQwLrhgjB6aZqs=")

if not credentials:
    print("Error: You must specify a configuration method")
    sys.exit(1)
try:
    stack = echoclient.YowsupEchoStack(credentials, True)
    stack.start()
except KeyboardInterrupt:
    print("\nYowsdown")
    sys.exit(0)