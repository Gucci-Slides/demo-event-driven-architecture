from tools.events_systems import dispatch


def create_user(username: str, password: str):
    print("User was saved: ", username, password)
    dispatch('user_registered', username)


def notify_friends(username: str):
    print("Friends were notified", username)


def email_friends(username: str):
    print("Email sent", username)
