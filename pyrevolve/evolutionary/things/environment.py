import os
import string

from pyrevolve.experiment.experiment_manager import ExperimentManager
from pyrevolve.evolutionary.algorithm.ecology.population import Population


class Environment:

    experiment_manager = ExperimentManager()

    def __init__(self, filename: string, population: Population = None):
        self.population: Population = population
        self.path: string = os.path.join(self.experiment_manager.world_path, filename)
