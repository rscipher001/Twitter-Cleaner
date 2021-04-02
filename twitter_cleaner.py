import json
import sys
import tweepy


def banner():
    print('''
 _____          _ _   _               ____ _
|_   _|_      _(_) |_| |_ ___ _ __   / ___| | ___  __ _ _ __   ___ _ __
  | | \ \ /\ / / | __| __/ _ \ '__| | |   | |/ _ \/ _` | '_ \ / _ \ '__|
  | |  \ V  V /| | |_| ||  __/ |    | |___| |  __/ (_| | | | |  __/ |
  |_|   \_/\_/ |_|\__|\__\___|_|     \____|_|\___|\__,_|_| |_|\___|_| v1.0
  ''')


def authenticate():
    # Create API global variable
    global api

    # Read credentials.json
    credentials = json.loads(open('credentials.json').read())

    # Set API related variables
    consumer_key = credentials['consumer_key']
    consumer_secret = credentials['consumer_secret']
    access_token = credentials['access_token']
    access_token_secret = credentials['access_token_secret']

    # Create tweepy auth variable
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # authorize
    api = tweepy.API(auth)

    return


def menu():
    print('''
1. Delete all tweets.
2. Delete all likes
3. Delete all DMs.
4. Exit.''')


def delete_all_tweets():
    print("\nDeleting all tweets\n")

    # Get user detail
    me = api.me()
    print('Status Count: ', me.statuses_count, "\n")

    # 20 status retrieved once so count number of iteration 
    number_of_round = me.statuses_count // 20 + 1

    deleted = 0

    # Start Deleting
    for i in range(0, number_of_round):
        user_tweets = api.user_timeline()
        for tweet in user_tweets.ids():
            api.destroy_status(tweet)
            deleted = deleted + 1

    print(deleted, "/", me.statuses_count, " tweets deleted")
    return


def delete_all_likes():
    print("\nDeleting all likes\n")

    # Get user detail
    me = api.me()

    print('Likes Count: ', me.favourites_count)

    # counter
    unliked = 0

    number_of_round = me.favourites_count // 20 + 1

    # Start unliking
    for i in range(0, number_of_round):
        user_likes = api.favorites()
        for tweet in user_likes.ids():
            api.destroy_favorite(tweet)
            unliked = unliked + 1

    print(unliked, "/", me.favourites_count, " tweets unliked")
    return


def delete_all_direct_messages():
    # Retrive DMs to collect IDs
    dms = api.direct_messages()

    # Start Deleting
    for dm in dms.ids():
        api.destroy_direct_message(dm)

    return


def bye():
    print("\nHave a nice day!\n")
    sys.exit(0)


if __name__ == "__main__":
    banner()
    authenticate()
    menu()
    options = {
        '1': delete_all_tweets,
        '2': delete_all_likes,
        '3': delete_all_direct_messages,
        '4': bye
    }

    choice = input('\nChoice: ')
    options[choice]()
