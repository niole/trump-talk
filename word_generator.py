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
from content import CONTENT

def build_trans_matrix(text):
    """
    builds a histogram of all word pairs
    """
    words = text.split()
    total_words = len(words)
    unique_words = list(Set(words))
    transition_hist = defaultdict(int)

    #sliding window of 2
    for i in range(len(words)-1):
        transition_hist[words[i]+" "+words[i+1]] += 1


    #iterate over word set and build matrix
    matrix = [[0 for _ in unique_words] for _ in unique_words]

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
    prob = random.random()
    lb = 0

    for i in range(len(neighbors)):
        n = neighbors[i]
        ub = lb+n
        if (n > 0):
            if prob >= lb and prob <= ub:
                return i
            lb += n
    return int(math.floor(prob*len(neighbors)))

def should_move(new, old):
    prob = random.random()
    next_prob = new/old
    return prob <= min(1.0, next_prob)

def generate_words(trans_matrix, words, iterations):
    stationary_prob = [1 for _ in words]
    mcmc_result = defaultdict(int)
    pos = 0

    for _ in range(iterations):
        next_pos = get_next_pos(trans_matrix[pos])
        if (should_move(stationary_prob[next_pos], stationary_prob[pos])):
            pos = next_pos
        mcmc_result[words[pos]] += 1

    return mcmc_result

def get_generated_vs_data_error(mcmc_output, word_hist):
    #accept when difference is 10% or less
    subtracted = defaultdict(int)

    for key, value in mcmc_output.items():
        subtracted[key] = word_hist[key] - mcmc_output[key]

    return math.sqrt(reduce(lambda a, b: a+b, map(lambda x: x**2, [v for _, v in subtracted.items()])))

unique_words, matrix = build_trans_matrix(CONTENT)
word_hist = Counter(unique_words)
mm = generate_words(matrix, unique_words, 1000)
err = get_generated_vs_data_error(mm, word_hist)

print "err"
print err

print "mm"
print mm


