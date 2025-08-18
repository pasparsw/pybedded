# Introduction

**_PyBedded_** is an experimental utility which allows you to write code for Arduino with Python.

# How to use it?

Assuming that you have _pybedded_ cloned at the same level as your script, the first thing you need to do is to import necessary types from the _pybedded_ module:

```python
from src import *
```

Next, you start a Python block of Arduino code using `ArduinoBoard`. You must provide the port your Arduino is connected to and the specific board you're using, for example:

```python
with ArduinoBoard(port="/dev/ttyUSB0", board=Board.UNO):
```

Now, the entire logic you write within this block, will be flashed to the Arduino board. Bellow you can see the traditional blink example:

```python
from src import *

with ArduinoBoard("/dev/ttyUSB0", Board.UNO):
    def setup() -> None:
        pinMode(LED_BUILTIN, OUTPUT)


    def loop() -> None:
        digitalWrite(LED_BUILTIN, HIGH)
        delay(1000)
        digitalWrite(LED_BUILTIN, LOW)
        delay(1000)
```

You can read about _pybedded_ and how does it work in details this [this article](www.pikotutorial.com).

# Unsupported features

Because this an experimental project, not all features are supported yet, including:

