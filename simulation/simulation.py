import os
import numpy as np
import warnings
import tqdm
import socket
import datetime


class Simulation:
    def __init__(self, num_iterations, args={'stats_enabled': False}):
        self._agent_list = []
        self._descriptor_list = []
        self._stat_list = []
        self._num_iterations = num_iterations
        self._current_iteration = 0
        self._args = args

        if 'stats_enabled' in self._args.keys() and self._args['stats_enabled']:
            hostname = socket.gethostname()
            timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            self._dirname = hostname + '_' + timestamp
            if not os.path.exists(self._dirname):
                os.makedirs(self._dirname)

    def get_simu(self):
        return self

    def add_agent(self, agent):
        self._agent_list.append(agent)
        return self

    def add_descriptor(self, desc):
        self._descriptor_list.append(desc)
        return self

    def add_stat(self, stat):
        self._stat_list.append(stat)
        return self

    def get_num_agents(self):
        return len(self._agent_list)

    def get_agents(self):
        return self._agent_list

    def get_num_iterations(self):
        return self._num_iterations

    def get_current_iteration(self):
        return self._current_iteration

    def get_dirname(self):
        return self._dirname

    def get_descriptors(self):
        return self._descriptor_list

    def get_stats(self):
        return self._stat_list

    def _update(self):
        if 'stats_enabled' in self._args.keys() and self._args['stats_enabled']:
            for obj in self._stat_list:
                obj(self)

            for obj in self._descriptor_list:
                obj(self)

    def spin_once(self):
        for a in self._agent_list:
            a.run()

        if self._current_iteration > self._num_iterations:
            warnings.warn(
                'You have exceeded the number of iterations allocated for this simulation')

        self._current_iteration += 1

    def spin(self):
        for _ in tqdm.tqdm(range(self._num_iterations)):
            self.spin_once()
