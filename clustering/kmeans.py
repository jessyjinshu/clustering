from collections import defaultdict
from math import inf
from math import sqrt
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """

    new_p = []

    p_len = len(points)
    d_len = len(points[0])

    for d in range(d_len):
        sum = 0
        for p in range(p_len):
            sum = sum + points[p][d]
        
        new_p.append((float(sum))/(float(p_len)))
    
    return new_p


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """


    new_set = defaultdict(list)
    center = []
    
    

    for (assignment,point)in zip(assignments,data_set):
        new_set[assignment].append(point)
    
    for i in new_set.keys():
        center.append(point_avg(new_set[i]))


    return center


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    dim = len(a)

    sum = 0

    for d in range(dim):
        elem = (a[d]-b[d])**2
        sum = sum + elem
    
    return sqrt(sum)

    


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    if k<= 0 or k > len(data_set):
        raise ValueError("k is not valid")
    return random.sample(data_set,k)


def get_list_from_dataset_file(dataset_file):
    data = []

    with open(dataset_file) as f:
        datas = csv.reader(f)
        for l in datas:
            row = []
            for n in l:
                elem = int(n)
                row.append(elem)
            data.append(row)
    return data




def cost_function(clustering):
    c = 0

    for k in clustering.keys():
        lst = clustering[k]
        center_point = point_avg(lst)

        for p in lst:
            c = c + distance(center_point,p)
    
    return c



def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    print("hi")
    return clustering
