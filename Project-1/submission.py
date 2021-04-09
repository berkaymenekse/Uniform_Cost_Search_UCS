import csv
import math
from queue import PriorityQueue

# Pseudocode
#https://algorithmicthoughts.wordpress.com/2012/12/15/artificial-intelligence-uniform-cost-searchucs/
#Insert the root into the queue
#While the queue is not empty
#      Dequeue the maximum priority element from the queue
#      (If priorities are same, alphabetically smaller path is chosen)
#      If the path is ending in the goal state, print the path and exit
#      Else
#           Insert all the children of the dequeued element, with the cumulative costs as priority

class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)
class FileNotFoundError(Exception):
    def __init__(self):
        print("The path does not exist")
class PathNotFoundEror(Exception):
    def __init__(self,info):
        print("The path between %s does not exist in this universe. Try at another one." %info)

# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    Map = {}
    with open(path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        title_flag = 0
        for row in csv_reader:
            if not bool(title_flag):
                title_flag += 1
                continue
            if row[0] not in Map:
                Map[row[0]] = {}
            if row[1] not in Map:
                Map[row[1]] = {}
            # Bi directional road
            Map[row[0]][row[1]] = int(row[2])
            Map[row[1]][row[0]] = int(row[2])
            #print("From " + row[0] + " to " + str(Map[row[0]]))

    return Map


# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
    priority = 0

    p_queue = PriorityQueue()
    visited_nodes = []
    p_queue.put((priority, start,[start]))
    cumulative = 0


    while not p_queue.empty():

        city_tuple = p_queue.get()
        cumulative = city_tuple[0]
        city = city_tuple[1]
        road_way = city_tuple[2]


        visited_nodes.append(city)


        if (city == end):
            #print("yess")
            #print(visited_nodes)
            return
        else:
            #print("Else girdi")
            #print(city)
            # print(graph[city])
            for next in graph[city]:
                # print(next)
                if (next == end):
                    visited_nodes.append(next)
                    #print(visited_nodes)
                    min_distance = graph[city][next] + cumulative
                    print(min_distance)
                    print(road_way+[end])
                    return
                if next not in visited_nodes:
                    tempCity = next
                    tempCum = graph[city][next] + cumulative
                    #road_way.append(tempCity)
                    p_queue.put((graph[city][next] + cumulative, next,road_way + [next]))

    assert p_queue.empty()==False, (start, end)



# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    try:
        Graph = build_graph("data/cities.csv")
        uniform_cost_search(Graph, "İstanbul", "Antalya")
    except OSError:
        FileNotFoundError()
    except AssertionError as a:
        PathNotFoundEror(a.args)

