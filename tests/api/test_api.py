import requests
import pytest


# get request
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    print(response.text)
    # verify if status code is 200
    assert response.status_code == 200

    # verify if response contains data
    data = response.json()
    assert len(data) > 0  # Ensure that the list of users is not empty


# get request
def test_get_single_user():
    url = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1  # Verify that the user id is 1
    assert "name" in data  # Check if 'name' field exists


# post request to create a user
def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {"name": "John Doe",
               "username": "john_doe",
               "email": "john@example.com",
               "address": {
                   "street": "123 Main St",
                   "suite": "Apt. 4B",
                   "city": "New York",
                   "zipcode": "10001"}}

    response = requests.post(url, json=payload,
                             headers={"Content-Type": "application/json"})
    print(response.text)
    assert response.status_code == 201

    data = response.json()
    assert data['name'] == 'John Doe'
    assert data['username'] == 'john_doe'


# put request to update a user
def test_update_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    payload = {"name": "Jane DOE", "username": "jane_DOE"}

    response = requests.put(url, json=payload,
                            headers={"Content-Type": "application/json"})
    print(response.text)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane DOE"


# delete request to delete a user
def test_delete_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.delete(url)
    print(response.text)
    assert response.status_code == 200
    assert response.text == "{}"  # Response should be empty after successful delete
