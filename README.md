# Twitter Cleaner

```
 _____          _ _   _               ____ _
|_   _|_      _(_) |_| |_ ___ _ __   / ___| | ___  __ _ _ __   ___ _ __
  | | \ \ /\ / / | __| __/ _ \ '__| | |   | |/ _ \/ _` | '_ \ / _ \ '__|
  | |  \ V  V /| | |_| ||  __/ |    | |___| |  __/ (_| | | | |  __/ |
  |_|   \_/\_/ |_|\__|\__\___|_|     \____|_|\___|\__,_|_| |_|\___|_| v1.0
  

1. Delete all tweets.
2. Delete all likes
3. Delete all DMs.
4. Exit.
```
A very simple tool written in Python to clean your Twitter profile.

# How to use
* Get a developer account on Twitter [Click here](https://developer.twitter.com/en/apply-for-access) (May take up to 15 days) 
* Create a Twitter App (Assuming you've got a developer account)
* Clone this repository
* Copy your app credential to `credentials-sample.json`
* Rename `credentials-sample.json` to `credentials.json`
* Run it `python3 twitter_cleaner.py`

##### NOTE: You may have to run same operation more than once because Twitter doesn't seem to delete everything in one attempt.