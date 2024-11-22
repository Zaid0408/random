import requests

# Define the server URL
server_url = 'http://127.0.0.1:5000/users'

# 1. GET all users
response = requests.get(server_url)
print('GET all users:')
print(response.json())

# 2. GET a single user
user_id = 1
response = requests.get(f'{server_url}/{user_id}')
print(f'GET user with id {user_id}:')
print(response.json())

# 3. POST a new user
new_user = {"id": 4, "name": "David"}
response = requests.post(server_url, json=new_user)
print('POST new user:')
print(response.json())

# 4. PUT to update an existing user
updated_user = {"name": "Alice Updated"}
response = requests.put(f'{server_url}/1', json=updated_user)
print('PUT update user with id 1:')
print(response.json())

# 5. DELETE a user
response = requests.delete(f'{server_url}/2')
print('DELETE user with id 2:')
print(response.json())

# 6. GET all users again to see the changes
response = requests.get(server_url)
print('GET all users after changes:')
print(response.json())
