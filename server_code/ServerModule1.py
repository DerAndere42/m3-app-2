import anvil.server
import anvil.media
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (4056, 3040)

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def takepic():
  camera.capture('foo.jpg')
return anvil.media.from_file('foo.jpg')