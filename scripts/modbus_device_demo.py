#!/usr/bin/env python

### NO ROS FUNCTIONALITY INCLUDED ###


from __future__ import print_function

import logging
import json
import time

from modbus_device import ModbusSlaveDevice


logger = logging.getLogger('modbus_slave_demo')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


# run standalone
if __name__ == "__main__":
    with open("./slave.json") as config_file:
        config = json.load(config_file)

        slave = ModbusSlaveDevice(config)

        def make_print_callback(input):
            return lambda v: print(input.name, v)
        
        slave.attach_callbacks(make_print_callback)
        slave.connect()

        gripper_state = False

        while True:
            slave.read()
            time.sleep(0.5)
            slave.write("gripper", gripper_state)
            gripper_state = not gripper_state
    