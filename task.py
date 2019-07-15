import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 12
        self.action_low = 100
        self.action_high = 900
        self.action_size = 4
        self.runtime = runtime
        


        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 
        
        self.upp_bounds = self.target_pos + 2
        self.low_bounds = self.target_pos - 2

    def get_reward(self):
        """Uses current pose of sim to return reward."""

        distance = np.tanh(3. - 0.003*(abs(self.sim.pose[:3] - self.target_pos)).sum())
#         angular_vel = abs(np.tanh(self.sim.angular_v.sum()))
#         angles_pos = abs(np.tanh(self.sim.pose[3:].sum()))
#         height = self.sim.pose[2]
            
        reward = 1 + distance 

        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities                
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
            pose_all.append(self.sim.v)
            pose_all.append(self.sim.angular_v)
       
        condition =  (self.upp_bounds > self.sim.pose[:3]).all() and (self.sim.pose[:3]> self.low_bounds).all()
        if condition:
            print("Target reached!", end="")

            reward += 40
            done = True

        elif done:  
            if self.sim.pose[2] <= self.sim.lower_bounds[2]:
                print("Crashed!", end="")
                reward -= 20
            elif (self.sim.pose[:3] <= self.sim.lower_bounds).any() or (self.sim.pose[:3] >= self.sim.upper_bounds).any():
                print("Out!", end="")
            else:
                print("Time out!", end="")
                
                

                
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate((self.sim.pose, self.sim.v, self.sim.angular_v) * self.action_repeat)

        return state