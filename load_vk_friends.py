# -*- coding: utf-8 -*-

""" Program for loading friends graph from VK """

import vk_api
import networkx as nx

N = 5  # Максимальная глубина графа
M = 30 # Максимальное число друзей которое нужно вернуть
VK_LOGIN = 'kirainluck@gmail.com'
VK_TOKEN = 'ce373d45c3f69d93022b12d3e9af02916e22becd049aaeeb40de1c19e7a65a3e0e58945b1d547beab9e0b'
VK_IDS = [559640345, 29759351, 120435774, 78517271, 55564167,
         202514864, 79818398, 18214699, 25689500, 322913600]


def fill_graph(vk, graph, id, deep=1):
    print(deep)
    try:
        response = vk.friends.get(user_id=id, count=M)
    except vk_api.exceptions.ApiError:
        return

    for fr_id in response['items']:
        graph.add_edge(id, fr_id)
        if (fr_id not in VK_IDS) and (deep < N):
            deep += 1
            fill_graph(vk, graph, fr_id, deep)


def main():
    vk_session = vk_api.VkApi(login=VK_LOGIN, token=VK_TOKEN)
    vk = vk_session.get_api()
    friends_graph = nx.Graph()
    for id in VK_IDS:
        fill_graph(vk, friends_graph, id)


if __name__ == "__main__":
    main()
