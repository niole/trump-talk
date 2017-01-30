# pylint: disable-all
"""
take a paragraph, build a transition matrix based on
what words follow what other words
cardinality is the different words
make sure to normalize rows so that all rows equal 1

MCMC it
"""
from collections import defaultdict, Counter
from sets import Set
import random
import math


INITIAL_STATIONARY_PROB = .001
INITIAL_TRANS_PROB = 0

def build_trans_matrix(words):
    """
    words - [string]

    return [string], [[float]] - array of unique elements in words, transition matrix
    """
    total_words = len(words)
    unique_words = list(Set(words))
    transition_hist = defaultdict(int)

    #sliding window of 2
    for i in range(len(words)-1):
        transition_hist[words[i]+" "+words[i+1]] += 1


    #iterate over word set and build matrix
    #TODO don't include unattainable elements in a row of neighbors
    matrix = [[INITIAL_TRANS_PROB for _ in unique_words] for _ in unique_words]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            frm = unique_words[r]
            to = unique_words[c]
            matrix[r][c] = transition_hist[frm+" "+to]/total_words


    for r in range(len(matrix)):
        total_prob = sum(matrix[r])
        if total_prob > 0:
            for c in range(len(matrix[r])):
                #normalize each row to equal 1
                matrix[r][c] = matrix[r][c]/total_prob

    return unique_words, matrix

def get_next_pos(neighbors):
    """
    gets the index of the next element in Markov process

    neighbors - [float]

    return int
    """
    prob = random.random()
    lb = 0

    for i in range(len(neighbors)):
        n = neighbors[i]
        ub = lb+n
        if (n > 0):
            if prob >= lb and prob <= ub:
                return i
            lb += n

    #fallback
    return int(math.floor(prob*len(neighbors)))

def should_move(new, old):
    """
    new - float
    old - float

    return bool
    """

    prob = random.random()
    next_prob = new/old
    return prob <= min(1.0, next_prob)

def generate_markov_chain(trans_matrix, words, iterations, stationary_prob):
    """
    trans_matrix - [[int]]
    words - [string]
    iterations - int
    stationary_prob - [int]

    return [int] - normalized Markov Chain output
    """
    mcmc_result = [INITIAL_STATIONARY_PROB for _ in words]
    pos = 0

    for _ in range(iterations):
        next_pos = get_next_pos(trans_matrix[pos])
        if (should_move(stationary_prob[next_pos], stationary_prob[pos])):
            pos = next_pos
        mcmc_result[pos] += 1

    #normalize result
    total_appearances = sum(mcmc_result)

    return map(lambda x: x/total_appearances, mcmc_result)

def get_generated_vs_data_error(mcmc_output, word_hist):
    """
    mcmc_output - dict(string -> float)
    word_hist - dict(string -> int)

    return float - error between mcmc_output and word_hist
    """
    subtracted = defaultdict(int)

    for key, value in mcmc_output.items():
        subtracted[key] = word_hist[key] - mcmc_output[key]

    return math.sqrt(reduce(lambda a, b: a+b, map(lambda x: x**2, [v for _, v in subtracted.items()])))

def get_normed_word_histogram(words):
    """
    words - [string] all elements in original text, which was split on space

    return dict(string -> float) normed histogram of word occurences
    """
    total_words = float(len(words))
    word_hist = Counter(words)

    return { k: float(v)/total_words for k, v in word_hist.items() }

def solve_for_stationary_prob(total_iterations, iterations_per_mcmc, data):
    """
    generates stationary probability vector, which corresponds to
    appearance of each unique element in data

    total_iterations - int
    iterations_per_mcmc - int
    data - string

    return [string], [float]
    """

    words = data.split()
    unique_words, matrix = build_trans_matrix(words)
    word_hist = get_normed_word_histogram(words)
    word_location_hash = { index: unique_words[index] for index in range(len(unique_words)) }
    err = float("inf")
    best_prob_dist = [1 for _ in range(len(data))]

    for _ in range(total_iterations):
        mm = generate_markov_chain(matrix, unique_words, iterations_per_mcmc, best_prob_dist)
        mm_hist = { word_location_hash[index]: mm[index] for index in range(len(mm)) }
        next_err = get_generated_vs_data_error(mm_hist, word_hist)

        if (next_err < err):
            total = sum(mm)
            best_prob_dist = map(lambda x: x/total, mm)
            err = next_err

    return unique_words, best_prob_dist
