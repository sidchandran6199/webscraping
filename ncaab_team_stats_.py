import collections
import pandas as pd
import requests


###updates columns of df to only use abbreviation of stat
def update_columns(df):
    old_columns = list(df.columns.values)
    new_columns = []
    for col in old_columns:
        temp = col.split(" ")
        new_columns.append(temp[0])
    return new_columns


####returns a df based on specified stat(which is referenced in path of url)
def get_stat_df(url):
    html = requests.get(url).content
    df = pd.read_html(html)
    df = df[0]
    df.columns = update_columns(df)
    return df


###passing in a list of sorted dfs for a specific stat. teams are ranked based off of num teams in conf as processed through sorted manner
def rank_teams(df_list, num_teams):
    team_points = collections.Counter()
    for df in df_list:
        points = num_teams
        for index, row in df.iterrows():
            team = row['Team']
            team_points[team] += points
            points -= 1
    return team_points


####dynamically specifies urls for a specific conference.
def conference_dictionary(conf):
    urls = {
        'scoring': 'https://www.cbssports.com/college-basketball/stats/team/team/scoring/' + conf + '/',
        'rebounding': 'https://www.cbssports.com/college-basketball/stats/team/team/rebounds/' + conf + '/',
        'passing': 'https://www.cbssports.com/college-basketball/stats/team/team/assists-turnovers/' + conf + '/',
        'steals': 'https://www.cbssports.com/college-basketball/stats/team/team/steals/' + conf + '/',
        'blocks': 'https://www.cbssports.com/college-basketball/stats/team/team/blocks/' + conf + '/'
    }
    return urls


###creates sorted dfs for 3FG%, TOPG, RPG. Then returns teams ranked based off those 3 dfs per conf
def rank_3pt_rebounds_lowTurnovers(conf):
    urls = conference_dictionary(conf)
    best_3pt_df = get_stat_df(urls['scoring'])[['Team', '3FG%']].sort_values('3FG%', ascending=False)
    best_rebounding_df = get_stat_df(urls['rebounding'])[['Team', 'RPG']].sort_values('RPG', ascending=False)
    low_turnover_df = get_stat_df(urls['passing'])[['Team', 'TOPG']].sort_values('TOPG', ascending=True)
    num_teams = best_rebounding_df.shape[0]
    list_of_dfs = [best_3pt_df, best_rebounding_df, low_turnover_df]

    ranking = rank_teams(list_of_dfs, num_teams)
    return ranking

def rank_ppg_apg(conf):
    urls = conference_dictionary(conf)
    best_ppg_df = get_stat_df(urls['scoring'])[['Team', 'PPG']].sort_values('PPG', ascending=False)
    best_apg_df = get_stat_df(urls['passing'])[['Team', 'APG']].sort_values('APG', ascending=False)

    num_teams = best_ppg_df.shape[0]
    list_of_dfs = [best_ppg_df, best_apg_df]

    ranking = rank_teams(list_of_dfs, num_teams)
    return ranking

###merges rankings of power 5 conferences and sorts
def sort_power5(function_name):
    big10 = function_name('BIG10')
    acc = function_name('ACC')
    big12 = function_name('BIG12')
    pac12 = function_name('PAC12')
    sec = function_name("SEC")
    power5 = {**big10, **acc, **big12, **pac12, **sec}
    power5_sorted = dict(sorted(power5.items(), key=lambda item: item[1], reverse=True))
    return power5_sorted


if __name__ == '__main__':
    print(sort_power5(rank_3pt_rebounds_lowTurnovers))
    print(sort_power5(rank_ppg_apg))


