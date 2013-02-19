import requests, sys, json, getpass, datetime
from dateutil import parser
from pandas import Series, DataFrame
from collections import Counter

def fetch_members(username, password):
	users = requests.get("https://api.github.com/orgs/pythonkurs/members", auth=(username, password))
	users_data = users.json()
	return users_data

def fetch_repos(username, password):
	repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(username, password))
	repos_data = repos.json()
	return repos_data

## replacement for fetch_repos	
def get_repos(): 
	url = r'https://api.github.com/orgs/pythonkurs/repos'
	username = raw_input('username:')	
	password = getpass.getpass()
	repos_response = requests.get(url, auth=(username, password))
	repos = repos_response.json()
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
				commits_times += [parser.parse(commit['commit']['author']['date'])]
				# commits_times += [commit['commit']['author']['date']]
				commits_messages += [commit['commit']['message']]
		result[repo_name] = Series(commits_messages,index=commits_times)
	df = DataFrame(result)
	return df
	
def analyse(df):
	dict_weekday = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	dates = list(df.index)
	weekdays = []
	hours = []

	for entry in dates:
		weekdays.append(entry.weekday())
		hours.append(entry.hour)
		dict_week = Counter(week_day_list)
		dict_hour = Counter(hour_list)

	result = dict_weekday[week_dict.most_common(1)[0][0]] + 'is the most common day.' + str(dict_hour.most_common(1)[0][0]) +' is the most common hour.'
	return result

df = get_repos()
print analyse(df)