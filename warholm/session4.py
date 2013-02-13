import requests
from dateutil import parser
import datetime
from pandas import Series, DataFrame
import sys, json

def fetch_members(username, password):
	users = requests.get("https://api.github.com/orgs/pythonkurs/members", auth=(username, password))
	users_data = users.json()
	return users_data

def fetch_repos(username, password):
	repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(username, password))
	repos_data = repos.json()
	return repos_data

base = datetime.datetime.now()
date_list = [base - datetime.timedelta(days=x) for x in range(5)]

s = Series(["A commit message"] * 5, index=date_list, name="A repo")
df = DataFrame(s)


username = ''
password = ''

repos = fetch_repos(username,password)

result = {}
for repo in repos:
    repo_name =  repo['name']
    url_commits =  repo['commits_url'].replace('{/sha}','')
    commits = requests.get(url_commits,  auth=(username, password))
    commits_data = commits.json()
    
    commits_messages=[]
    commits_times=[]
    for commit in commits_data:
        if type(commit) == dict:
            commits_times += [commit['commit']['author']['date']]
            commits_messages += [commit['commit']['message']]

        result[repo_name] = Series(commits_messages,index=commits_times)
df = DataFrame(result)


print df