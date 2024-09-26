import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class TwistListener(Node):

    def __init__(self):
        super().__init__('twist_listener')
        self.subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.listener_callback,
            10
    	)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f"Twist - linear: ({msg.linear.x}, {msg.linear.y}, {msg.linear.z}), angular: ({msg.angular.x}, {msg.angular.y}, {msg.angular.z})")


def main(args=None):
    rclpy.init(args=args)

    twist_listener = TwistListener()

    rclpy.spin(twist_listener)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    twist_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
