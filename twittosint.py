#!/usr/bin/env python3

import sys
import os
import re
from collections import Counter
from prettytable import PrettyTable
import argparse
import tweepy

CONSUMER_KEY=os.getenv('CONSUMER_KEY')
CONSUMER_SECRET=os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN=os.getenv('BEARER_TOKEN')

client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="target username", type=str)
parser.add_argument("-p", "--profile-information", help="Get profile information of a user", action="store_true")
parser.add_argument("-ht", "--hashtag", help="Get user recently used hashtags", action="store_true")
parser.add_argument("-c", "--comparison", help="Compare users network", type=str)
parser.add_argument("-m", "--mentions", help="Get people the user has mentioned the most", action="store_true")
parser.add_argument("-f", "--followers", help="Get user followers details", action="store_true")
parser.add_argument("-l", "--limit", help="Number of results wanted", type=str)
args = parser.parse_args()

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

def banner():
	print('''
                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)	
               (_/ .  \  :           / l      c"~o \

                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//TwittOSINT
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  (( by S1rN3tZ
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll
                / .  .  . : | :!        \\ 
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"

	''')


def profile(username):
	description = client.get_users(usernames=username, user_fields=['description','created_at','location','url','profile_image_url'])
	for user in description.data:
		print(f'''
  Profile
-----------------------------------------------

username: {user.username}	

avatar: 
{user.profile_image_url}
 
biography: 
{user.description}
	
location: {user.location}
	
website: {user.url}

account created at: {user.created_at}
		''')

def hashtags(username):
	user=client.get_user(username=username)
	userID=user.data.id
	print(bcolors.INFO+"[*] "+bcolors.RESET+"The twitter ID of "+bcolors.INFO+username+bcolors.RESET+" is "+str(userID))

	tweets = client.get_users_tweets(userID, max_results=100)
	hashtag_list=[]
	ht_list=[]
	if not tweets.data:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No recent tweet found.")
	else:		
		for tweet in tweets.data:
			string=tweet.text
			for word in string.split():
				if word[0] == '#':
					hashtag_list.append(word[0:])
		print(bcolors.INFO+"[*] "+username+bcolors.RESET+" is interested in:")
		if not hashtag_list:
			print(bcolors.FAIL+"[!] "+"Target didn't recently use hashtag.")
		else:	
			for hashtag in hashtag_list:
				if hashtag not in ht_list:
					ht_list.append(hashtag)
			for ht in ht_list:
				print(ht)
def mention(username):
	user=client.get_user(username=username)
	userID=user.data.id
	print(bcolors.INFO+"[*] "+bcolors.RESET+"The twitter ID of "+bcolors.INFO+username+bcolors.RESET+" is "+str(userID))

	tweets = client.get_users_tweets(userID, max_results=100)
	mention_list=[]
	contact_list=[]
	if not tweets.data:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No recent tweet found.")
	else:
		for tweet in tweets.data:
			string=tweet.text
			for word in string.split():
				if word[0] == '@':
					mention_list.append(word[0:])
		print(bcolors.INFO+"[*] "+username+bcolors.RESET+"'s mentions:\n")
		if not mention_list:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"No recent mention found.")
		else:
			occurence=Counter(mention_list)
			ordered=sorted(occurence.items(), key=lambda t: t[1], reverse=True)
			result=dict(ordered)
			for key, value in result.items():
				print(bcolors.OK+"[+] "+bcolors.RESET+key+" with "+str(value)+" mention(s)")
	
def InCommon(first_username, second_username):
	user1=client.get_user(username=first_username)
	user2=client.get_user(username=second_username)

	user1ID=user1.data.id
	user2ID=user2.data.id

	print(bcolors.INFO+"[*] "+bcolors.RESET+"The twitter ID of "+bcolors.INFO+first_username+bcolors.RESET+" is "+str(user1ID))
	print(bcolors.INFO+"[*] "+bcolors.RESET+"The twitter ID of "+bcolors.INFO+second_username+bcolors.RESET+" is "+str(user2ID)+"\n")

	first_following = client.get_users_following(user1ID, max_results=1000)
	second_following = client.get_users_following(user2ID, max_results=1000)
	first_followers = client.get_users_followers(user1ID, max_results=1000)
	second_followers = client.get_users_followers(user2ID, max_results=1000)
	
	flw_count = 0
	flwr_count = 0
	following_first_list = []
	following_second_list = []
	follower_first_list = []
	follower_second_list = []
	
	try:
		for follow in first_following.data:
			following_first_list.append(follow.username)
		for follow2 in second_following.data:
			following_second_list.append(follow2.username)
	except:
		pass

	print(bcolors.INFO+"[*] "+bcolors.RESET+"following in common:\n")
	for flw in following_first_list:
		if flw in following_second_list:
			flw_count=flw_count+1
			print(flw)

	try:
		for follower in first_followers.data:
			follower_first_list.append(follower.username)
		for follower2 in second_followers.data:
			follower_second_list.append(follower2.username)
	except:
		pass

	print("\n"+bcolors.INFO+"[*] "+bcolors.RESET+"followers in common:\n")
	for flwr in follower_first_list:
		if flwr in follower_second_list:
			flwr_count=flwr_count+1
			print(flwr)
	print("\n"+bcolors.INFO+"[*] "+first_username+bcolors.RESET+" and "+bcolors.INFO+second_username+bcolors.RESET+" have "+str(flw_count)+" follows and "+str(flwr_count)+" followers in common")

def followers(username):
	user=client.get_user(username=username)

	userID=user.data.id
	print(bcolors.INFO+"[*] "+bcolors.RESET+"The twitter ID of "+bcolors.INFO+username+bcolors.RESET+" is "+str(userID))
	print(bcolors.INFO+"[*] "+bcolors.RESET+"Processing your request...")
	print(bcolors.INFO+"[*] "+bcolors.RESET+"It may take more or less time depending on the set limit.")
	if args.limit:
		limit = args.limit
	else:
		limit=1000
	followers = client.get_users_followers(userID, max_results=limit)
	regex = r"\W([\w\-\.]+@[\w\-\.]+)+\W"
	
	t=PrettyTable(['Follower', 'Email', 'Location'])

	try:
		for follower in followers.data:
			infos = client.get_users(usernames=follower.username, user_fields=['description','location'])
			for user in infos.data:
				match = re.findall(regex,str(user.description))
				if not match:
					match=bcolors.FAIL+"None"+bcolors.RESET
				t.add_row([follower.username,str(match),user.location])
		print(t)
	except Exception as e:
		print(e)
	
def main():
	if args.comparison:
		try:
			usernames=args.comparison.split("/")
			u1 = usernames[0]
			u2 = usernames[1]
			InCommon(u1,u2)
		except:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"Error syntax")
			help()
			exit(0)

	if args.username:
		username=args.username
		if args.hashtag:
			hashtags(username)
		if args.profile_information:
			profile(username)
		if args.mentions:
			mention(username)
		if args.followers:
			followers(username)

if __name__ == '__main__':
	try:
		banner()
		main()
	except Exception as e:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
		print(e)
	except KeyboardInterrupt:
	       	print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
