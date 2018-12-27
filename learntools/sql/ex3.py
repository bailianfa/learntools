import pandas as pd
from learntools.core import *


class ProlificCommenters(EqualityCheckProblem):
    _var = 'prolific_commenters_query'
    correct_answer = pd.DataFrame({'author': {0: 'dragonwriter',
  1: None,
  2: 'eru',
  3: 'rbanffy',
  4: 'DanBC',
  5: 'sp332',
  6: 'davidw',
  7: 'rayiner',
  8: 'tptacek',
  9: 'jacquesm',
  10: 'jrockway',
  11: 'anigbrowl',
  12: 'stcredzero'},
 'NumPosts': {0: 10723,
  1: 227736,
  2: 10448,
  3: 10557,
  4: 12902,
  5: 10882,
  6: 10764,
  7: 11080,
  8: 33839,
  9: 21107,
  10: 13626,
  11: 11395,
  12: 10092}})
    _expected = correct_answer
    _solution = CS(\
"""
prolific_commenters_query = \"""SELECT author, COUNT(id) numposts
            FROM `bigquery-public-data.hacker_news.comments`
            GROUP BY author
            HAVING COUNT(id) > 10000
        \"""
""" 
)

class NumDeletedPosts(EqualityCheckProblem):
    _var = 'num_deleted_posts'
    _expected = 227736
    _solution = CS(\
"""
deleted_posts_query = \"""SELECT COUNT(id) num_deleted_posts
            FROM `bigquery-public-data.hacker_news.comments`
            WHERE deleted = True
        \"""
deleted_posts_results = hacker_news.query_to_pandas_safe(deleted_posts_query)
num_deleted_posts = 227736
"""
)

class AnyAggregationQuery(CodingProblem):
    _vars = ['my_query', 'my_results']
    def check(self, query, results):
        assert (type(query) == str), ("You don't have a valid query")
        assert ('select' in query.lower()), ("You don't have a valid query. It doesn't even have the word SELECT in it.")
        assert ('from' in query.lower()), ("You don't have a valid query. It doesn't even have the word FROM in it.")
        assert (type(results) == pd.DataFrame), ("You haven't successfully executed a query to get results in `my_results`")
    _solution = CS(\
"""
my_query = \"""SELECT author, MIN(time_ts) first_comment, MAX(time_ts) last_comment
            FROM `bigquery-public-data.hacker_news.comments`
            GROUP BY author
        \"""
hacker_news.query_to_pandas_safe(my_query)
"""
)



qvars = bind_exercises(globals(), [
    ProlificCommenters,

    ],
    tutorial_id=79,
    var_format='q_{n}',
    )

__all__ = list(qvars)