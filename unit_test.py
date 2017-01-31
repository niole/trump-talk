# pylint: disable-all
from word_generator import solve_for_stationary_prob, build_trans_matrices, get_words


INPUT = """
cats cats cats cats cats cats dogs dogs dogs parrots
"""

expected = { 'cats': 0.6, 'dogs': 0.3, 'parrots': 0.1 }

top_level_total_iter = 1000
total_iter = 1000
error = .01
unique_data, parameters = solve_for_stationary_prob(top_level_total_iter, total_iter, INPUT)

for i in range(len(parameters)):
    parameter = parameters[i]
    assert abs(expected[unique_data[i]] - parameter) <= error, "parameter should be within expected error"


def test_build_trans_matrices(actual, expected):
    for i in range(len(actual)):
        for j in range(len(actual[i])):
            for k in range(len(actual[i][j])):
                assert abs(expected[i][j][k] - actual[i][j][k]) <= error, "actual should equal expected within certain error"
trans_hash_1 = { 'cats cats': 6.0, 'cats dogs': 1.0, 'cats parrots': 0.0, 'dogs dogs': 2.0, 'dogs cats': 0.0, 'dogs parrots': 1.0, 'parrots parrots': 0.0, 'parrots dogs': 0.0, 'parrots cats': 0.0 }
trans_hash_2 = { 'cats cats': 4.0, 'cats dogs': 2.0, 'cats parrots': 0.0, 'dogs dogs': 1.0, 'dogs cats': 0.0, 'dogs parrots': 1.0, 'parrots parrots': 0.0, 'parrots dogs': 0.0, 'parrots cats': 0.0 }
word_location_hash, unique_words, trans_matrices = build_trans_matrices(get_words(INPUT), 2)
trans_matrix_1


expected = [word for word in unique_words]
test_build_trans_matrices(trans_matrices, expected)
