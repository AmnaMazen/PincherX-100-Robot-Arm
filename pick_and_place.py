
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def main():

    # Make instance of InterbotixManipulatorXS
    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )
    bot.arm.go_to_home_pose()
    
    bot.arm.set_single_joint_position(joint_name='waist', position=np.pi/2.0)

    bot.arm.set_ee_cartesian_trajectory(z=-0.1)

    bot.gripper.grasp(2.0)

    bot.arm.set_single_joint_position(joint_name='waist', position=np.pi/4.0)

    bot.gripper.release(2.0)

    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

    bot.shutdown()


if __name__ == '__main__':
    main()