from random import randint


def reservoir_sample(seq, k):
    """
    https://en.wikipedia.org/wiki/Reservoir_sampling

    Reservoir sampling is a family of randomized algorithms for randomly choosing a sample of k items from a list S
    containing n items, where n is either a very large or unknown number. Typically n is large enough that the list
    doesn't fit into main memory.
    """
    sample = [0] * k
    for i in range(k):
        sample[i] = seq[i]
    for i, s in enumerate(seq):
        j = randint(0, i)
        if j < k:
            sample[j] = s
    return sample


def mean(iterable):
    return sum(iterable) / len(iterable)

res = reservoir_sample(xrange(1000000), k=1000)
print mean(res)
