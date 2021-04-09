#python libraries
import tweepy
import csv
import random
import string
import time, sys
import multiprocessing

#Load keys and tokens from a file within the same directory
keys = open("twitter-database-keys.txt", "r")
consumer_key = keys.readline().rstrip('\n')
consumer_secret = keys.readline().rstrip('\n')
access_token = keys.readline().rstrip('\n')
access_token_secret = keys.readline().rstrip('\n')
keys.close()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def start():
#Test authentication
    try:
        api.verify_credentials()
        print("Auth success")
    except:
        print("Auth fail")    

#Query string and number of iterations
    querys = input("Twitter search query: ")
    items = int(input("Number of iterations: "))
    return querys, items

def tweetsf(querys, items):
    #Column names 
    coltweet = ['tweet_id', 'user_id', 'content', 'posted_on', 'edited_on']
    filename = 'tweets.csv'
    with open (filename, 'a+', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(coltweet)
        for tweet in tweepy.Cursor(api.search, q=querys).items(items):
            tweets_encoded = tweet.text.encode('utf-8')
            tweets_decoded = tweets_encoded.decode('utf-8')
            csvWriter.writerow([tweet.id_str, tweet.user.id_str, tweet.text, tweet.created_at, tweet.created_at])
    #Write immediatly to disk
    sys.stdout.flush()

def usersf(querys, items):
    #Column names
    colusr = ['user_id', 'email', 'pass', 'username', 'display_name', 'joined_on']
    #Get data from the tweets file
    with open("tweets.csv", "r", encoding="utf-8", newline='') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',')
        userid = []
        for lines in csv_reader:
            userid.append(lines['user_id'])
    #Create users file        
    filename = 'users.csv'
    with open (filename, 'a+', encoding="utf-8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        csvWriter = csv.writer(csv_file)
        csvWriter.writerow(colusr)        
        i = 0
        while i < len(userid):
            csvWriter.writerow([''+userid[i], ''+rmail(10), ''+rpass(10), ''+api.get_user(userid[i]).screen_name, ''+api.get_user(userid[i]).name,  ''+str(api.get_user(userid[i]).created_at)])
            i += 1
            
def followf(querys, items):
    #Column names 
    colfol = ['user_id', 'follower_id']
    #Get data from the users file
    with open("tweets.csv", "r", encoding="utf-8", newline='') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',')
        userid = []
        for lines in csv_reader:
            userid.append(lines['user_id'])    
    #Create followers file, limit followers list per user to 10
    filename = 'followers.csv'
    with open (filename, 'a+', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(colfol)
        i = 0
        followid = []
        while i < len(userid):
            c = 0            
            for page in tweepy.Cursor(api.followers_ids, api.get_user(userid[i]).screen_name).pages():
                followid.extend(page)
                while c < 10:
                    csvWriter.writerow([''+userid[i], ''+str(followid[c])])    
                    c += 1
            i += 1

def retweetf(querys, items):
    #Column names            
    colret = ['user_id', 'is_comment', 'tweet_id', 'comment_id', 'retweeted_on']
    #tweetid == comment_id because twitter search shows only tweets or comments to a tweet
    #retweetid == 'N/A'. it's just part of the SQL scheme, address this later
    #RT ids are random... 
    
    #Get data from the tweets file
    with open("tweets.csv", "r", encoding="utf-8", newline='') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',')
        tweetid = []
        for lines in csv_reader:
            tweetid.append(lines['tweet_id'])
    #Create retweets file
    filename = 'retweets.csv'
    with open (filename, 'a+', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(colret)
        i = 0
        while i< len(tweetid):
            csvWriter.writerow([''+rID(8), 'n', ''+str(tweetid[i]), ''+str(tweetid[i]), ''+str(api.get_status(tweetid[i]).created_at)])
            i += 1

def likef(querys, items):
    #Column names            
    collik = ['user_id', 'is_comment', 'tweet_id', 'comment_id', 'liked_on']
    #tweetid == comment_id because twitter search shows only tweets or comments to a tweet
    #likeid == 'N/A'. it's just part of the SQL scheme, address this later
    #Like ids are random... 
    
    #Get data from the tweets file
    with open("tweets.csv", "r", encoding="utf-8", newline='') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',')
        tweetid = []
        for lines in csv_reader:
            tweetid.append(lines['tweet_id'])
    #Create retweets file
    filename = 'likes.csv'
    with open (filename, 'a+', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(collik)
        i = 0
        while i< len(tweetid):
            csvWriter.writerow([''+rID(8), 'n', ''+str(tweetid[i]), ''+str(tweetid[i]), ''+str(api.get_status(tweetid[i]).created_at)])
            i += 1
    
def commentf(querys, items):
    #Column names            
    colcom = ['user_id', 'tweet_id', 'posted_on', 'edited_on']
    #commentid == 'N/A'. it's just part of the SQL scheme, address this later
    #comment ids are random... 
    
    #Get data from the tweets file
    with open("tweets.csv", "r", encoding="utf-8", newline='') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',')
        tweetid = []
        for lines in csv_reader:
            tweetid.append(lines['tweet_id'])
    #Create retweets file
    filename = 'comments.csv'
    with open (filename, 'a+', encoding="utf-8", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(colcom)
        i = 0
        while i< len(tweetid):
            csvWriter.writerow([''+rID(8), 'n', ''+str(tweetid[i]), ''+str(api.get_status(tweetid[i]).created_at), ''+str(api.get_status(tweetid[i]).created_at)])
            i += 1 
    
#(This won't be relevant for this project) Generate random emails and passwords, duplicates don't matter.
def rmail(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))+'@gmail.com'
    return result_str

def rpass(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

#Random ID generator
def rID(length):
    numbers = string.digits
    result_str = ''.join(random.choice(numbers) for i in range(length))
    return result_str

#Run in parallel:
if __name__ == '__main__':
    data1, data2 = start()   
    tweetsf(data1, data2)
    usersf(data1, data2)
    followf(data1, data2)
    p1 = multiprocessing.Process(target=retweetf, args=(data1, data2))
    p2 = multiprocessing.Process(target=likef, args=(data1, data2))
    p3 = multiprocessing.Process(target=commentf, args=(data1, data2))
    p1.start()
    p2.start()
    p3.start()
