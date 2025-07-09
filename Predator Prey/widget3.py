### Written by Andy Sheu ###
### BIO 1B -- DS MODULES ###

import numpy as np
import pandas as pd
import ipywidgets as widgets
from IPython.display import clear_output
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def simulate_predation(parameters):
    if parameters['predator_population'] == 0 or parameters['prey_population'] == 0:
        return 0
    predator_population = parameters['predator_population']
    prey_rate = min(1, parameters['prey_population'] / parameters['carrying_capacity'])
    return np.random.binomial(predator_population, prey_rate)

def advance_generation(parameters, prey_eaten):
    L = max(0, parameters['prey_population'] - prey_eaten)
    K = parameters['carrying_capacity']
    parameters['prey_population'] = int(L + (parameters['prey_reproduction_rate'] * L * (K-L)/K))
    parameters['predator_population'] = int(prey_eaten / parameters['predator_birth_constant']) if prey_eaten > 0 else 0

def populations_simulate(parameters):
    population_df = pd.DataFrame(columns=['Generation', 'Predator', 'Prey']).set_index('Generation')
    population_df.loc[0] = [parameters['predator_population'], parameters['prey_population']]
    for generation in np.arange(1, 1 + parameters['generations']):
        prey_eaten = simulate_predation(parameters)
        advance_generation(parameters, prey_eaten)
        population_df.loc[generation] = [parameters['predator_population'], parameters['prey_population']]
    return population_d


# Intentionally creating merge conflict
