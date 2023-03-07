from tools.events_systems import register_event
from tools.services import create_user, notify_friends, email_friends


register_event('user_registered', notify_friends)
register_event('user_registered', email_friends)
create_user('demo-larry', 'password')
create_user('demo-thomas', 'password2')
create_user('demo-james', 'password3')
