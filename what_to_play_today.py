import sqlite3


class MDZZ():
    def __init__(self):
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

    def random_select_sqlite(self,
                             lower_bound=None,
                             upper_bound=None,
                             difficulty=None,
                             category=None):
        # STARS
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
        selected_stars = self.full_stars_list[low:upper + 1]

        # DIFFICULTY
        selected_difficulty = []
        if difficulty == 'Any':
            selected_difficulty = self.difficulty_list
        elif difficulty == 'Master+Re':
            selected_difficulty = ['Master', 'Re:Master']
        else:
            selected_difficulty = [difficulty]

        # OPEN SQL CONNECTION
        conn = sqlite3.connect('maimai_info.db')
        c = conn.cursor()

        # BUILD QUERY STR
        stars_query_str = "("
        for star in selected_stars:
            stars_query_str += "'%s'," % (star)
        stars_query_str = stars_query_str[:-1]
        stars_query_str += ")"

        difficulty_query_str = "("
        for diff in selected_difficulty:
            difficulty_query_str += "'%s'," % (diff)
        difficulty_query_str = difficulty_query_str[:-1]
        difficulty_query_str += ")"

        category_query_str = "("
        for cate in category:
            category_query_str += "'%s'," % (cate)
        category_query_str = category_query_str[:-1]
        category_query_str += ")"

        full_query_str = " \
            SELECT CATEGORY, MUSIC_NAME, DIFFICULTY, STARS \
            FROM MAIMAI_MUSIC_INFO \
            WHERE STARS IN %s AND DIFFICULTY IN %s AND CATEGORY IN %s \
            ORDER BY RANDOM() limit 1;\
        " % (stars_query_str, difficulty_query_str, category_query_str)

        # QUERY
        cursor = c.execute(full_query_str)
        query_result = cursor.fetchall()
        conn.close()
        # RETURN RESULT
        if len(query_result) == 0:
            return -1
        else:
            return query_result[0]
