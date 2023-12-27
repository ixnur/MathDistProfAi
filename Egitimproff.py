import numpy as np
import joblib
import random

learning_rate = 0.1
discount_factor = 0.9
exploration_prob = 1.0  
exploration_decay = 0.99

class MathEnvironment:
    def __init__(self, target_number):
        self.target_number = target_number
        self.current_result = np.random.randint(1, 100)
        self.operators = ['+', '-', '*', '/', 'sqrt', 'pow', 'mod', 'factorial', 'sin', 'cos', 'tan', 'log', 'abs', 'cbrt', 'exp', 'ceil', 'floor']
        self.action_space_size = len(self.operators)

    def take_action(self, action):
        operator = self.operators[action]
        state = [self.current_result, action]
        if abs(self.current_result - self.target_number) < 5:
            reward = 1
        elif abs(self.current_result - self.target_number) < 10:
            reward = 0.5
        else:
            reward = 0
        if operator == '+':
            self.current_result += np.random.randint(1, 10)
        elif operator == '-':
            self.current_result -= np.random.randint(1, 10)
        elif operator == '*':
            self.current_result *= np.random.randint(2, 5)
        elif operator == '/':
            divisor = np.random.randint(2, 5)
            self.current_result = self.current_result // divisor if self.current_result % divisor == 0 else self.current_result
        elif operator == 'sqrt':
            self.current_result = np.sqrt(self.current_result)
        elif operator == 'pow':
            self.current_result = np.power(self.current_result, np.random.randint(2, 4))
        elif operator == 'mod':
            self.current_result %= np.random.randint(2, 5)
        elif operator == 'factorial':
            self.current_result = np.math.factorial(int(self.current_result))
        elif operator == 'sin':
            self.current_result = np.sin(self.current_result)
        elif operator == 'cos':
            self.current_result = np.cos(self.current_result)
        elif operator == 'tan':
            self.current_result = np.tan(self.current_result)
        elif operator == 'log':
            self.current_result = np.log(self.current_result) if self.current_result > 0 else 0
        elif operator == 'abs':
            self.current_result = np.abs(self.current_result)
        elif operator == 'cbrt':
            self.current_result = np.cbrt(self.current_result)
        elif operator == 'exp':
            self.current_result = np.exp(self.current_result)
        elif operator == 'ceil':
            self.current_result = np.ceil(self.current_result)
        elif operator == 'floor':
            self.current_result = np.floor(self.current_result)
        return state, reward
    
def q_learning_algorithm(env, q_table, num_episodes=1000, model_filename='math_model'):
    for episode in range(num_episodes):
        state = [env.current_result, random.randint(0, env.action_space_size - 1)]  
        total_reward = 0

        while True:
            if np.random.rand() < exploration_prob:
                action = random.randint(0, env.action_space_size - 1)
            else:
                action = np.argmax(q_table[tuple(state)])

            next_state, reward = env.take_action(action)
            best_future_q = np.max(q_table[tuple(next_state)])
            q_table[tuple(state)][action] = (1 - learning_rate) * q_table[tuple(state)][action] + learning_rate * (reward + discount_factor * best_future_q)

            total_reward += reward
            state = next_state

            model_filename_episode = f"{model_filename}_episode_{episode}.joblib"
            joblib.dump(q_table, model_filename_episode)

            print(f"Episode {episode + 1}, Action: {env.operators[action]}, Current state: {env.current_result}")

            if reward == 1:
                break  
        exploration_prob *= exploration_decay

    print("Training finished. Total reward:", total_reward)


target_number = 2  
q_table = np.zeros((100, env.action_space_size))
env = MathEnvironment(target_number)
q_learning_algorithm(env, q_table)
