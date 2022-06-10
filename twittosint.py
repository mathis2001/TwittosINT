import sys
from sys import argv
import os
import tweepy

CONSUMER_KEY=os.getenv('CONSUMER_KEY')
CONSUMER_SECRET=os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN=os.getenv('BEARER_TOKEN')


client = tweepy.Client( consumer_key=CONSUMER_KEY, 
                        consumer_secret=CONSUMER_SECRET,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET,
                        bearer_token=BEARER_TOKEN,
                        wait_on_rate_limit=True)

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

def help():
	print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./twittosint.py [-h] -u username [-ht] [-p]")
	print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./twittosint.py [-h] -c username1/username2")
	print('''
  Options
  -------------------------------------------
	-u   target username
	-p   profile informations
	-ht  hashtags used by the target
	-c   followers and following comparison
  -------------------------------------------
	''')

def getopts(argv):
	opts = {}  
	while argv:
		try:
			if argv[0][0] == '-':
				opts[argv[0]] = argv[1] 
		except:
			if argv[0] == '-h':
				help()
				exit(0)
		argv = argv[1:] 
	return opts

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
	for tweet in tweets.data:
		string=tweet.text
		for word in string.split():
			if word[0] == '#':
				hashtag_list.append(word[0:])
	print(bcolors.INFO+"[*] "+username+bcolors.RESET+" is interested in:")
	for hashtag in hashtag_list:
		print(hashtag)
		
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

def main():
	myargs = getopts(argv)
	if len(sys.argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No option given.")
		help()
		exit(0)
	elif '-c' in myargs:
		try:
			usernames=myargs['-c'].split("/")
			u1 = usernames[0]
			u2 = usernames[1]
			InCommon(u1,u2)
		except:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"Error syntax")
			help()
			exit(0)

	elif '-u' in myargs:
		username=myargs['-u']
		if '-ht' in argv:
			hashtags(username)
		if '-p' in argv:
			profile(username)


if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
		print(e)
	except KeyboardInterrupt:
        	print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
