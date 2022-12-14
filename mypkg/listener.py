# SPDX-FileCopyrightTest: 2022 Aika katsuki
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from person_msg.msg import Person

def cb(msg):
    global node
    node.get_logger().info("Listen: %s"% msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cb, 10)

rclpy.spin(node)

