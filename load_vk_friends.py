# -*- coding: utf-8 -*-

""" Program for loading friends graph from VK """

import vk_api
import networkx as nx

MAX_DEEP = 3  # Max graph deep
MAX_FRIENDS = 30 # Max number of friends vk method can process
VK_LOGIN = 'kirainluck@gmail.com'
VK_TOKEN = 'ce373d45c3f69d93022b12d3e9af02916e22becd049aaeeb40de1c19e7a65a3e0e58945b1d547beab9e0b'
VK_IDS = [
    559640345, 29759351, 120435774, 78517271, 55564167,
    202514864, 79818398, 18214699, 25689500, 322913600,
    32418429, 32784038, 55355150, 65817487, 76637395,
    31710423, 557916962, 44907648
]

GRAPH_FILENAME = 'friends_graph.yaml'

def fill_graph(vk, graph, id, deep=1):
    max_cnt = MAX_FRIENDS
    # usually all friends are found on the 1st level
    if deep == 1:
        max_cnt = 500
    try:
        response = vk.friends.get(user_id=id, count=max_cnt)
    except vk_api.exceptions.ApiError as e:
        print(f"VK api error on id {id} and deep {deep}\n {e}")
        return

    fr_in_lst = False
    for fr_id in response['items']:
        graph.add_edge(id, fr_id)
        if fr_id in VK_IDS:
            fr_in_lst = True
    if (not fr_in_lst) and (deep < MAX_DEEP):
        deep += 1
        for fr_id in response['items']:
            fill_graph(vk, graph, fr_id, deep)


def main():
    vk_session = vk_api.VkApi(login=VK_LOGIN, token=VK_TOKEN)
    vk = vk_session.get_api()
    friends_graph = nx.Graph()
    for id in VK_IDS:
        print(id)
        fill_graph(vk, friends_graph, id)

    print(f"Number of nodes: {friends_graph.number_of_nodes()}")
    # writing graph to file
    nx.readwrite.nx_yaml.write_yaml(friends_graph, GRAPH_FILENAME)

    #loaded_friends_graph = nx.readwrite.nx_yaml.read_yaml(GRAPH_FILENAME)
    #print(list(loaded_friends_graph.neighbors(559640345)))

if __name__ == "__main__":
    main()
