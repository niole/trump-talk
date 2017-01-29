# pylint: disable-all
from word_generator import solve_for_parameters


INPUT = """
cats cats cats cats cats cats dogs dogs dogs parrots
"""

expected = { 'cats': 0.6, 'dogs': 0.3, 'parrots': 0.1 }

top_level_total_iter = 1000
total_iter = 1000
error = .01
unique_data, parameters = solve_for_parameters(top_level_total_iter, total_iter, INPUT)

for i in range(len(parameters)):
    parameter = parameters[i]
    assert parameter >= expected[unique_data[i]] - error, "parameter should be lower bounded by expected minus error"
    assert parameter <= expected[unique_data[i]] + error, "parameter should be upper bounded by expected minus error"


