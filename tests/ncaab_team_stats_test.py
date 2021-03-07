from ncaab_team_stats_ import get_stat_df, update_columns, rank_teams, conference_dictionary, \
    rank_3pt_rebounds_lowTurnovers
import unittest

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

    def test_rank_3pt_rebounds_lowTurnovers(self):
        ranking = rank_3pt_rebounds_lowTurnovers('ACC')
        assert ranking['Virginia'] == 32
        assert ranking ['Syracuse'] == 31
        assert ranking ['Florida St.'] == 30



if __name__ == '__main__':
     unittest.main()
