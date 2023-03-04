from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import csv

list = "Season, Episode, Rating \n"

# Goes through all 7 seasons
for i in range(1,8):
	# Downloading the webpage information
	url = 'https://www.imdb.com/title/tt1826940/episodes?season=%s' % i
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')

	# Find all the episodes
	episodes = soup.find_all('div', {'class': 'info'})

	# Scrape the ratings of every episode
	for k, episode in enumerate(episodes, start=1):
		rating = episode.find('span', {'class': 'ipl-rating-star__rating'}).text
		season = i
		episode_num = k
        
		if episode_num < 10:
			episode_num = episode_num / 10

		list = list + (f'{season} + {episode_num}, {rating}') + "\n"

# print(list)

# Split the data into a list of lists
data_list = [row.split(', ') for row in list.split('\n')]

# Open a new CSV file in write mode
with open('ratings.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    for row in data_list:
        writer.writerow(row)
