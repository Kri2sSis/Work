from collections import deque

graph = {'Ruslan':[]}

def person_is_seller(person):
    pass

def serch_graph(name):
    serch_deque = deque()
    serch_deque += graph[name]
    check_list = []
    while serch_deque:
        person = serch_deque.popleft()
        if not person in check_list:
            if person_is_seller(person):
                print(person+"is a seller mango")
                check_list.append(person)
                return True
        else:
            serch_deque+= graph[person]
            check_list.append(person)
        return False


serch_graph('Ruslan')