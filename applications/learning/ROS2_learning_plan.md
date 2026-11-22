# ROS 2 Learning Plan for Arunabha (about 3 weeks, 30-60 min a day)

Goal: be able to say honestly in interviews "I can build a small ROS 2 system: nodes, topics, a robot model,
simulation and recorded data", and connect it to what I already do (sensors, sync, test setups).

## Week 0: Setup (1-2 evenings)
- Use ROS 2 **Jazzy** (the current long-term support version) on **Ubuntu 24.04**.
- On Windows: install Ubuntu through WSL2, or use the official ROS 2 Docker image. On a spare laptop: dual-boot Ubuntu.
- Install: follow "Installation" on the official docs: https://docs.ros.org/en/jazzy/Installation.html
- Check it works: run the talker/listener demo from the docs.

## Week 1: The basics (official beginner tutorials)
Official tutorials: https://docs.ros.org/en/jazzy/Tutorials.html
| Day | Topic | Try this |
|---|---|---|
| 1 | Configuring environment, turtlesim | Drive the turtle with the keyboard |
| 2 | Nodes | `ros2 node list`, `ros2 node info` |
| 3 | Topics | `ros2 topic echo`, `ros2 topic pub`, `rqt_graph` |
| 4 | Services and parameters | Change the turtle's background colour with a parameter |
| 5 | Actions | Send a rotate goal to the turtle |
| 6 | Launch files | Start two turtles with one launch file |
| 7 | Recording data with **rosbag** | Record the turtle's pose, play it back (this is exactly "data collection") |

## Week 2: Write your own code (Python)
| Day | Topic | Try this |
|---|---|---|
| 8 | Create a workspace and package (colcon) | Build an empty package |
| 9 | Publisher and subscriber in Python | A node that publishes a fake joint angle, another that prints it |
| 10 | Custom messages | A message with angle, torque and time |
| 11 | Timers and rates | Publish at 100 Hz, measure the real rate |
| 12 | Time stamps and syncing two topics | Use message_filters to sync two sensor topics (like my Qualisys + robot sync) |
| 13 | Arduino to ROS 2 | Read an Arduino over serial and publish it as a topic (or try micro-ROS later) |
| 14 | Review | Draw the node graph of my mini system in rqt_graph |

## Week 3: Robots in ROS 2
| Day | Topic | Try this |
|---|---|---|
| 15 | URDF (robot description) | Write a simple 2-link arm, view it in RViz |
| 16 | joint_state_publisher, robot_state_publisher, TF | Move the arm joints with sliders in RViz |
| 17 | Gazebo simulation | Spawn the arm in Gazebo |
| 18 | ros2_control (intro) | Run a joint position controller on the simulated arm |
| 19 | Mini project part 1 | Model a simple version of my 5-bar robot in URDF |
| 20 | Mini project part 2 | Publish its joint states and record them with rosbag |
| 21 | Put it online | Push the code to github.com/arunabha22 with a short README and a screenshot |

## Free learning resources (check links)
- Official ROS 2 docs and tutorials (main source): https://docs.ros.org/en/jazzy/Tutorials.html
- YouTube: **Articulated Robotics** (very clear ROS 2 series for building real robots): search "Articulated Robotics ROS 2"
- YouTube: **Robotics Back-End** (beginner ROS 2 tutorials): search "Robotics Back-End ROS 2"
- When stuck: ROS Discourse (discourse.ros.org) and Robotics Stack Exchange

## How to talk about it after the plan
"I learned ROS 2 with the official tutorials and built a small project: a URDF model of a 5-bar robot in simulation,
publishing joint states and recording them with rosbag, plus an Arduino sensor node. It is on my GitHub."
(Only say this once it is actually done.)

## Tips
- Little and often beats long weekends: 30 minutes every day.
- Type the code yourself instead of copying, and write down every error and its fix.
- Link everything back to my own work: sensors, syncing, test setups and data.
