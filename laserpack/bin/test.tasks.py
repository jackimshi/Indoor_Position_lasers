from tasks import *
import rospy

rospy.init_node('test_tasks')
Controller = taskController()
task = test("Myname", 1)
Controller.addTask(task)
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()
Controller.rate.sleep()
Controller.spinOnce()