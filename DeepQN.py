import tensorflow as tf
from tensorflow import keras as k
import numpy as np
import collections as col


#DEEP LEARNING Q NETWORK

#first need state and action variables

action_size = 3
state_size = 20

#for gradient decent
batch_size = 32

#iterations of data
episodes = 1000

#DQN AGNENT

class DQN:

    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.memory = col.deque(maxlen=2000)

        self.gamma = 0.95

        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

        self.learning_rate = 0.001

        self.model = self._build_model()

    def _build_model(self):

        model = k.Sequential()

        model.add(k.layers.Dense(24, input_dim = self.state_size, activation='relu'))
        model.add(k.layers.Dense(24, activation='relu'))
        model.add(k.layers.Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=k.optimizers.Adam(lr=self.learning_rate))

        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append(state, action, reward, next_state, done)

    def act(self, state):
        if np.randon.rand() <= self.epsilon:
            return np.random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):

        minibatch = np.random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target

            self.model.fit(state, target_f, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon += self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)