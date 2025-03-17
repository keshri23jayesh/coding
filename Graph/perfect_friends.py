
friends_graph = [[1],
                 [0],
                 [3],
                 [2],
                 [5],
                 [4,6],
                 [5]]
visited = set()

def get_components(friend):
    stack = list()
    stack.append(friend)

    component = [friend]
    visited.add(friend)

    while stack:
        elem = stack.pop()
        for nbr in friends_graph[elem]:
            if nbr not in visited:
                component.append(nbr)
                stack.append(nbr)
                visited.add(nbr)
    return component


def perfect_friends():
    components = []
    for friend in range(0, len(friends_graph)):
        if friend not in visited:
            component = get_components(friend)
            components.append(component)
    print(components)

    total_pairs = 0
    for i in range (0, len(components)):
        for j in range(i+1, len(components)):
            total_pairs += len(components[i]) * len(components[j])

    print(total_pairs)

perfect_friends()