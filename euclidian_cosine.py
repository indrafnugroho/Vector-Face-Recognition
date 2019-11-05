import math

def euclidian_distance(v1, v2) :
    sum = 0
    for v1, v2 in zip(v1, v2) :
        sum += (v1-v2)**2
    distance = math.sqrt(sum)
    return distance

def dot_product(v1, v2) :
    sum = 0
    for v1, v2 in zip(v1, v2) :
        sum += v1*v2
    return sum

def norm(v) :
    sum = 0
    for i in range(len(v)) :
        sum += v[i]**2
    norm = math.sqrt(sum)
    return norm

def cosine_similarity(v1, v2) :
    dot = dot_product(v1, v2)
    normv1 = norm(v1)
    normv2 = norm(v2)
    cos = dot / (normv1*normv2)
    return cos