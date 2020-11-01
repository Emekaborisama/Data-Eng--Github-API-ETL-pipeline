import requests as r
import pprint as pprint
from github import Github
import pandas as pd
import numpy as np

# or using an access token
g = Github("ce0b6b0658bd5f3d3fc7072bf497a6897d07de18")

#create a loading pipeline 
import requests
from pprint import pprint

# github username
username = "risenW"


#check validation

    #url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
user = g.get_user(username)
for repo in user.get_repos():
    reposs = repo
    lan = repo.language
    l = str(lan)
    data = {'name': user_data['name'],
              'num_repo' : user_data['public_repos']
               }
df = pd.DataFrame(data, columns = ['name','num_repo'],index=[0])
print(df)
engine = sqlalchemy.create_engine(DATABASE_LOCATION)
conn = sqlite3.connect('my_played_tracks.sqlite')
cursor = conn.cursor()
sql_query = """CREATE TABLE IF NOT EXISTS my_played_tracks(
        name VARCHAR(200),
        repo VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (name, repo)
    )
    """
cursor.execute(sql_query)
print("Opened database successfully")
try:
    df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
except:
    print("Data already exists in the database")
    conn.close()
    print("Close database successfully")
  #



#load to a google big query datawarehouse









