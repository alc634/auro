# Echo a Turtlesim Topic

* Set up listener to listen to Twist with the current topic named `/turtle1/cmd_vel`

```
self.create_subcription(
  Twist,
  '/turtle1/cmd_vel',
  self.listener_callback,
  10
)
```

* Log info from topic

```
def listener_callback(self, msg):
  self.get_logger().info('cmd_vel value: %s' % msg.data
```

# Public Data to a Turtlesim Topic

* Set up a publisher to public data to the current topic name `/turtle1/cmd_vel`

```
self.create_publisher(
  Twist,
  '/turtle1/cmd_vel',
  10
)
timer_period = 0.5
self.timer = self.create_timer(timer_period, self.timer_callback)
```

* Publish data

```
def timer_callback(self):
  t_data = Twist()
  t_data.data = "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
  self.publisher_.publish(t_data)
  self.get_logger().info('Updating Turtlesim Twist: "%s"' % t_data.data)
```
