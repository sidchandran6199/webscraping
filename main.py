# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from nba_players_stats import create_nba_player_csv, create_df


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df_player_stats = create_df()
    create_nba_player_csv(df_player_stats)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
