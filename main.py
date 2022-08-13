from methods import *
import pandas as pd

def main(json_file_path, method):
  raw_tweets = pd.read_json(json_file_path, lines=True)
  raw_tweets = raw_tweets[raw_tweets['lang']=='en']

  print(method(raw_tweets))


if __name__ == "__main__":
  # Here you can change the method used
  main('farmers-protest-tweets-2021-03-5.json', top_10_users)