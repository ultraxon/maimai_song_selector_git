import pandas as pd
import numpy as np


class MDZZ():
    def __init__(self, data_info):
        self.full_song_info = data_info
        self.full_stars_list = [
            '1', '2', '3', '4', '5', '6', '7', '7+', '8', '8+', '9', '9+',
            '10', '10+', '11', '11+', '12', '12+', '13', '13+', '14'
        ]
        self.lower_bound = '1'
        self.upper_bound = '14'
        self.difficulty_list = [
            'Basic', 'Advanced', 'Expert', 'Master', 'Re:Master'
        ]
        self.category_list = [
            '流行＆动漫', 'niconico＆VOCALOID', '东方Project', '综艺节目', '原创乐曲'
        ]

    def random_select(self,
                      lower_bound=None,
                      upper_bound=None,
                      difficulty=None,
                      category=None):
        # BASED ON STARS: REQUIRED
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound

        low = self.full_stars_list.index(self.lower_bound)
        upper = self.full_stars_list.index(self.upper_bound)
        if upper < low:
            tmp = upper
            upper = low
            low = tmp

        selected_info = self.full_song_info[self.full_song_info.Stars.isin(
            self.full_stars_list[low:upper + 1])]

        # BASED ON DIFFICULTY: OPTIONAL
        if difficulty is not None and difficulty != 'Any':
            difficulty_to_query = [difficulty]
            if difficulty == 'Master+Re':
                difficulty_to_query = ['Master', 'Re:Master']
            selected_info = selected_info[selected_info.Difficulty.isin(
                difficulty_to_query)]

        # BASED ON CATEGORY
        if category is not None:
            selected_info = selected_info[selected_info.Category.isin(
                category)]

        if len(selected_info) != 0:
            random_result = selected_info.sample(frac=(1 / len(selected_info)))
            return [
                random_result['Category'].values[0],
                random_result['Music_name'].values[0],
                random_result['Difficulty'].values[0],
                random_result['Stars'].values[0]
            ]
        else:
            return -1
