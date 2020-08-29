# This instagram bot is created by KD-03
import sys
from InstagramAPI import InstagramAPI


def GetAllFollowing(bot, user_id):
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = bot.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(bot.LastJson.get('users', []))
        next_max_id = bot.LastJson.get('next_max_id', '')
    following = set([_['pk'] for _ in following])
    return following


def GetAllFollowers(bot, user_id):
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = bot.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(bot.LastJson.get('users', []))
        next_max_id = bot.LastJson.get('next_max_id', '')
    followers = set([_['pk'] for _ in followers])
    return followers

uid=input("Enter the username : ")
pasw=input("Enter the password : ")
ig=InstagramAPI(uid,pasw)
success=ig.login()
if not success:
	print("INSTAGRAM LOGIN FAILED !!!")
	sys.exit()
else:
	print("Welcome to Instagram Bot ")
	print("Username : "+uid)
ig.getSelfUsernameInfo()
self_id=ig.LastJson['user']['pk']

followers=GetAllFollowers(ig,self_id)
following=GetAllFollowing(ig,self_id)
print('- following {} users'.format(len(following)))
print('-followed by {} users'.format(len(followers)))

unreciprocated = following - followers

free_followers = followers - following

print('- following {} users that dont follow back'.format(len(unreciprocated)))
print('- you have {} followers that you dont follow back\n'.format(len(free_followers)))

print('Unfollowers are : ')
for _ in list(unreciprocated)[:min(len(unreciprocated),100)]:
        ig.getUsernameInfo(str(_))
        print('  -  {}'.format(ig.LastJson['user']['username']))

choice=input("Do you want unfollow this followers Yes/No : ")
if choice==("Yes" or "yes"):
	for _ in list(unreciprocated)[:min(len(unreciprocated), args.num_unfollows)]:
	       ig.getUsernameInfo(str(_))
	       print('  - unfollower user is {}'.format(ig.LastJson['user']['username']))
	       ig.unfollow(str(_))
else:
	sys.exit()