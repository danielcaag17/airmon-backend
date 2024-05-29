from collections import defaultdict

chats = defaultdict(lambda: 0)


def add_user(chat_name):
    chats[chat_name] += 1


def remove_user(chat_name):
    chats[chat_name] -= 1


def get_users_in_chat(chat_name):
    return chats[chat_name]
