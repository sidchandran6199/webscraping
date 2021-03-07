from ncaab_team_stats_ import get_stat_df, update_columns, rank_teams, conference_dictionary, \
    rank_3pt_rebounds_lowTurnovers
import unittest
import pandas as pd
class MyTest(unittest.TestCase):

    def setUp(self):
        self.df = get_stat_df('https://www.cbssports.com/college-basketball/stats/team/team/blocks/ACC/')

    def test_update_columns(self):
        new_columns = update_columns(self.df)
        assert new_columns == ['Team', 'Conf', 'GP', 'BLK', 'BPG']

    def test_get_stat_df(self):
        assert self.df is not None
        assert self.df.shape[0] == 15
        assert self.df.shape[1] == 5

    def test_conference_dictionary(self):
        urls = conference_dictionary('ACC')
        assert urls['scoring'] == 'https://www.cbssports.com/college-basketball/stats/team/team/scoring/ACC/'
        assert urls['rebounding'] == 'https://www.cbssports.com/college-basketball/stats/team/team/rebounds/ACC/'
        assert urls['passing'] == 'https://www.cbssports.com/college-basketball/stats/team/team/assists-turnovers/ACC/'
        assert urls['steals'] == 'https://www.cbssports.com/college-basketball/stats/team/team/steals/ACC/'
        assert urls['blocks'] == 'https://www.cbssports.com/college-basketball/stats/team/team/blocks/ACC/'

    def rank_teams_test(self):
        test_data_1 = [['virgina', 10], ['florida', 5], ['florida st.', 3]]
        test_data_2 = [[['florida', 10], ['florida st.', 5], ['virginia', 3]]]

        df_test_1 = pd.DataFrame(test_data_1, columns = ['Team', 'Stat'])
        df_test_2 = pd.DataFrame(test_data_2, columns = ['Team', 'Stat'])

        df_list = [df_test_1, df_test_2]

        scoring_dict = rank_teams(df_list, 3)
        assert scoring_dict['virgina'] == 4
        assert scoring_dict['florida'] == 5
        assert scoring_dict['florida st.'] == 3






if __name__ == '__main__':
     unittest.main()
