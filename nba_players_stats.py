import requests
from bs4 import BeautifulSoup
import pandas as pd
import heapq


def clean_url(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


def create_table(html_page):
    table = html_page.find_all(class_="full_table")
    all_players_stats = []

    for row in table:
        player = []
        for stat in row.find_all("td"):
            player.append(stat.text)
        all_players_stats.append(player)
    return all_players_stats


def create_columns(html_page):
    head = html_page.find(class_='thead')
    column_names_raw = [head.text for item in head][0]
    return column_names_raw.replace("\n", ",").split(",")[2:-1]


def create_df():
    html_page = clean_url('https://www.basketball-reference.com/leagues/NBA_2021_per_game.html')
    table = create_table(html_page)
    clean_columns = create_columns(html_page)
    return pd.DataFrame(table, columns=clean_columns)


def create_nba_player_csv(df):
    df.to_csv('2021_nba_player_stats', header=True)


def get_top_statistics(pq, n):
    heapq.heapify(pq)
    n_players = []
    for i in range(n):
        stat, person = heapq.heappop(pq)
        n_players.append([person, stat * -1])
    return n_players


def get_worst_statistics(pq, n):
    heapq.heapify(pq)
    n_players = []
    for i in range(n):
        stat, person = heapq.heappop(pq)
        n_players.append([person, stat * 1])
    return n_players


def top_three_point_shooters():
    df = create_df()
    three_point_df = df[['Player', '3P%', '3PA']]
    pq = []
    for index, row in three_point_df.iterrows():
        name = row['Player']
        percentage = row['3P%']
        attempts = row['3PA']
        if percentage and attempts:
            if float(attempts) > 3:
                pq.append([float(percentage) * -1, name])

    return get_top_statistics(pq, 10)


print(top_three_point_shooters())
