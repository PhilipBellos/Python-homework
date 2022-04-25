import pytest
import requests
import json
class TestPerson(object):

#1.Register a new user
#Register new user

    def test_register_1user(self):

        data = {
            "name": "Firstuserr",
            "email": "first.uuser@gmail.com",
            "password": "123456"
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/registration", headers=headers, data=json.dumps(data))

        assert r.status_code == 200
        print(r.json())

#Check that the new user can log in
    def test_login_1user(self):
        data = {
            "email": "first.uuser@gmail.com",
            "password": "123456"
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/login", headers=headers, data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())

#2.Register a new user with an existing email address
    def test_register_2user(self):

        data = {
            "name": "Seconduser",
            "email": "firsttt.user@gmail.com",
            "password": "654321"
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/registration", headers=headers, data=json.dumps(data))

        assert r.status_code == 200
        print(r.json())

#3.Create a new user + check user data
#3.1 Register a new (third) user
    def test_register_3user(self):

        data = {
            "name": "Philipovich",
            "email": "phillipovich36@gmail.com",
            "password": "1234768"
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/registration", headers=headers, data=json.dumps(data))

        assert r.status_code == 200
        print(r.json())

#3.2 Log in new user   ?
    @pytest.fixture()
    def test_login_3user(self):
        data = {
            "email": "phillipovich36@gmail.com",
            "password": "1234768"
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/login", headers=headers, data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())
        user_token = r.json()['data']['Token']
        yield user_token

#3.3 Create new user
    def test_create_1user(self, test_login_3user):
        user_token = test_login_3user
        data = {
            "name": "user36",
            "email": "userTraveler36@gmail.com",
            "location": "Kyiv"
        }
        headers = {
            "Authorization": "Bearer " + user_token,
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/users", headers=headers, data=json.dumps(data))
        assert r.status_code == 200 or 201
        print(r.json())
        user_id = r.json()['id']


#3.4 Check user data
        r = requests.get(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers)
        assert r.status_code == 200 or 201
        assert r.json()['name'] == "user36"
        print(r.json())

#4.Update user
#4.1 створення нового юзера використовуючи токен який отримали коли залогінився третій


#4.2 Modify some existing user
    def test_update_2user(self, test_login_3user):

        #create user
        user_token = test_login_3user
        data = {
            "name": "alexbellot",
            "email": "alexbellotTraveler4@gmail.com",
            "location": "Kyiv"
        }
        headers = {
            "Authorization": "Bearer " + user_token,
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/users", headers=headers, data=json.dumps(data))
        assert r.status_code == 200 or 201
        print(r.json())
        user_id = r.json()['id']
        r = requests.get(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers)
        assert r.status_code == 200 or 201

        #update user
        data = {
            "id": user_id,
            "name": "newalexbellot",
            "email": "alexbellotTraveler4@gmail.com",
            "location": "Kyiv"
        }
        headers = {
            "Authorization": "Bearer " + user_token,
            "Content-type": "Application/json"
        }
        r = requests.put(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers,
                         data=json.dumps(data))
        assert r.status_code == 200 or 201
        #get updated user

#4.2 Check your modifications
        r = requests.get(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers)
        assert r.status_code == 200 or 201
        assert r.json()['name'] == "newalexbellot"
        print(r.json())

