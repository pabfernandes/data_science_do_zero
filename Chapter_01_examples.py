users = [
        {"id": 0, "Name": "Hero"},
        {"id": 1, "Name": "Dunn"},
        {"id": 2, "Name": "Sue"},
        {"id": 3, "Name": "Chi"},
        {"id": 4, "Name": "Thor"},
        {"id": 5, "Name": "Clive"},
        {"id": 6, "Name": "Hicks"},
        {"id": 7, "Name": "Devin"},
        {"id": 8, "Name": "Kate"},
        {"id": 9, "Name": "Klein"}
        ]

friendship_pairs = [(0,1),
                    (0,2),
                    (1,2),
                    (1,3),
                    (2,3),
                    (3,4),
                    (4,5),
                    (5,6),
                    (5,7),
                    (6,8),
                    (7,8),
                    (8,0)]

# inicializando o dict com uma lista vazia para cada ID de usuário:
friendships = {user["id"]: [] for user in users}

# Em seguida, execute um loop pelos pares de amigos para preenchê-la:
for i, j in friendship_pairs:

    friendship[i].append(j) # Adicione i como amigo do usuário j
    friendship[j].append(i) # Adicione j como amigo do usuário i

def number_of_friends(user):
    """Quandos amigos tem o _user_?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                        for user in users)

# em seguida dividir pelo númeo de usuários
num_users = len(users)
avg_connections = total_connections / num_users

# Crie uma lista (user_id, number_of_friends)
num_friends_by_id = [(user["id"],
                    number_of_friends(user))
                     for user in users]

num_friends_by_id.sort(
        key = lambda
        id_and_friends: id_and_friends[1],
        reverse = True)

