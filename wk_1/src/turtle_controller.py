import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(
			Twist, 
        	'/turtle1/cmd_vel', 
        	10
    	)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        twist = Twist()
        
        twist.linear.x = 2.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 1.8

        self.publisher_.publish(twist)
        self.get_logger().info('Updating Turtlesim Twist.')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
