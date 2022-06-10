import redis
from redis.commands.json.path import Path

client = redis.Redis(host='localhost', port=6379, db=0)

jane = [{
     'name': "Girish", 
     'Age': 44, 
     'Location': "Nellai"
   },
{
     'name': "Mango", 
     'Age': 24, 
     'Location': "Chennai"
   },
{
     'name': "Latha", 
     'Age': 24, 
     'Location': "Bangalore"
   },
{
     'name': "Priya", 
     'Age': 14, 
     'Location': "Trivandrum"
   },
{
     'name': "Bhavana", 
     'Age': 34, 
     'Location': "Thrissur"
   }
];

client.json().set('accounts:1', Path.root_path(), jane)

result = client.json().get('accounts:1')
print(result)
