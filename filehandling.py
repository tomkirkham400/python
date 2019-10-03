with open("file.txt", "r") as f:
 for line in f:
   if "12345" in line:
     print(line)

import json

with open('output.json', 'r', encoding='utf8', errors='ignore') as json_file:  
    data = json.load(json_file)
    for tweet in data:
      if "liberals" in tweet["text"]:
        print("Created at:", tweet['created_at'])
        print("Tweet:", tweet['text'])
        print(tweet['user']['name'])
        print()

