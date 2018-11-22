from opytimizer import Opytimizer
from opytimizer.core.space import Space
from opytimizer.functions.internal import Internal
from opytimizer.optimizers.pso import PSO

import numpy as np


def test(x):
    sum = 0

    for array in x:
        value = np.linalg.norm(array)
        sum += value ** 2

    return sum


# Input parameters
n_agents = 5
n_variables = 5
n_dimensions = 1
n_iterations = 10

# Bounds parameters
# Note that it has to have the same size as n_variables
lower_bound = [0.1, 0.3, 0.5, 0.5, 0.5]
upper_bound = [0.2, 0.4, 2.0, 2.0, 2.0]

# Creating Space
s = Space(n_agents=n_agents, n_iterations=n_iterations,
          n_variables=n_variables, n_dimensions=n_dimensions,
          lower_bound=lower_bound, upper_bound=upper_bound)

# One should declare a hyperparameters object based
# on the desired algorithm that will be used
hyperparams = {
    'w': 2.5
}

# Creating PSO's optimizer
p = PSO(hyperparams=hyperparams)

# Creating Internal's function
f = Internal(pointer=test)

# Finally, we can create an Opytimizer class
o = Opytimizer(space=s, optimizer=p, function=f)

# Running
o.start()