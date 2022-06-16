# TwittosINT
A simple Twitter OSINT tool written in python

## Install:
```bash
$ git clone https://github.com/mathis2001/TwittosINT

$ cd TwittosINT

$ python3 twittosint.py
```
## Requirements:

- Python3

- Pip3

- tweepy

```bash
$ pip3 install tweepy
```

## Usage:
```bash
hashtags/profiler: ./twittosint.py [-h] -u username [-ht] [-p] [-m] [-f] [-l limit]
network comparison: ./twittosint.py [-h] -c username1/username2

```
## options:
```bash
Options
  -------------------------------------------
	-u   target username
	-p   profile information
	-ht  hashtags used by the target
	-c   followers and following comparison
	-m   check for mentions (occurence)
	-f   print followers details
	-l   limit
  -------------------------------------------

  Config 
        
        First, you have to create an application on https://developer.twitter.com/.
        Then, copy your tokens and paste them in your environment variables as 'CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET'
        and 'BEARER_TOKEN'.

```
## Configuration:

In order to use this tool, you have to create an app on https://developer.twitter.com/ to have access to your tokens and access keys.
It is necessary to use the free twitter APIv2.

Steps:

- create an app on your first log in developer.twitter.com.
- Once you are in your dashboard, go to 'Projects & App' > YOUR_PROJECT.

![image](https://user-images.githubusercontent.com/40497633/173073516-15390f60-e63d-4e1a-b431-a135c63a56b2.png)
- Go to 'Keys and tokens'.

![image](https://user-images.githubusercontent.com/40497633/173073920-b07666e1-2f79-4db0-bf30-2788ff2dada3.png)
- Finally, generate your access keys and tokens > add them to your environment variables.

## Some screens

![image](https://user-images.githubusercontent.com/40497633/173357103-c8c4f03c-a5c1-4159-b91a-6adcc23c6124.png)

![tempsnip](https://user-images.githubusercontent.com/40497633/173075972-083ee916-e1a6-485f-b339-5775ffded5d1.png)

![tempsnip](https://user-images.githubusercontent.com/40497633/173076312-3e46ea75-abe1-41c8-b55c-24f90c4d0e99.png)

![tempsnip](https://user-images.githubusercontent.com/40497633/173076890-4e4fa858-38b9-4c6f-98d3-79cb73006618.png)

![tempsnip](https://user-images.githubusercontent.com/40497633/173352166-1bc1b27e-77f5-4a1d-aa4c-d64059da3bd2.png)

![image](https://user-images.githubusercontent.com/40497633/173357906-81c37cd0-ae85-47a2-91c4-1612937ed394.png)

![image](https://user-images.githubusercontent.com/40497633/174047399-76163f57-9392-49ac-8110-bc7772d1c560.png)

