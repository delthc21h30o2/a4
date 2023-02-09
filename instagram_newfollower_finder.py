import instaloader

import getpass

L=instaloader.Instaloader()

f=open("followes.txt","r")

old_followers=[]

for line in f:
    old_followers.append(line)
f.close



username=input("enter username: ")
password=getpass.getpass("enter password: ")

L.login(username,password)

print("successfully logged in")

profile=instaloader.Profile.from_username(L.context,username)

now_followers=[]

for follower in profile.getfollowers():
    now_followers.append(follower)


# for old_follower in old_followers:
#     if old_follower not in now_followers:

#         print(old_follower)

for now_follower in now_followers:
    if now_follower not in old_followers:
        print(now_follower)

f=open("followers.txt","w")

for follower in now_followers:
    f.write(follower+ "/n")
f.close
