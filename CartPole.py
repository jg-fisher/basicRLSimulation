# basic CartPole simulation

import gym

env = gym.make('CartPole-v0') # create the environment

def basic_policy(obs): # determines what action to take
    angle = obs[2]
    return 0 if angle < 0 else 1

totals = [] # list of the total reward accumulated for each episode, 10

for episode in range(10):
    episode_rewards = 0 # the rewards for the episode, in this case just "staying alive" or running as long as possible
    obs = env.reset() # initial obersevation, carts horizontal positon (0.0 for center), carts velocity, pole angle, angular velocity (how fast the pole is falling)  
    action = 1 # move the cart left or right
    for step in range (1000): # 1000 total steps, dont want to run forever
        action = basic_policy(obs) # perform an action based on the policy and oberserved env
        env.render()
        obs, reward, done, info = env.step(action) # update the oberservations and reward with the action
        episode_rewards += reward # add the reward at the current time step, 1 in this case
        if done:
            totals.append(episode_rewards)
            break

print(totals)
print('The longest number of timesteps the pole was balanced: ' + str(max(totals)))
    


