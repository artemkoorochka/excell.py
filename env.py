import os
import sys

# Set environment variables
os.environ['login'] = 'username'
os.environ['password'] = 'secret'

# Get environment variables
print("Login: {}".format(os.getenv('login')))
print("Password: {}".format(os.environ.get('password')))
print("Command line argument: 1: {}, 2: {}".format(sys.argv[0], sys.argv[1]))