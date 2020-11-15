import os

def before_all(context):
    # Get and set some environment variables
    if 'base_url' in context.config.userdata:
        context.base_url = context.config.userdata['base_url']
    else:
        context.base_url = os.getenv('BASE_URL', 'http://127.0.0.1')
    if 'username' in context.config.userdata:
        context.username = context.config.userdata['username']
    else:
        context.username = os.getenv('USERNAME', 'user@example.com')
    if 'password' in context.config.userdata:
        context.password = context.config.userdata['password']
    else:
        context.password = os.getenv('PASSWORD', 'secret')
