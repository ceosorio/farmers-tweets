import pandas as pd

def top_10_retweeted(data):
  retweet_count = data.nlargest(10, 'retweetCount')
  return retweet_count['content', 'retweetCount']

def top_10_users(data):
  users = pd.json_normalize(data['user'])
  users.drop(['description', 'linkTcourl', 'url'], axis=1, inplace=True)
  users = pd.DataFrame(users)
  users.drop_duplicates(subset=['username'], inplace=True)
  usernames = []

  for user in data['user']:
      username = user['username']
      usernames.append(username)
  data['username'] = usernames
  
  return data['username'].value_counts().head(10)

def top_10_days(data):
  pass

def top_10_hashtags(data):
  pass