test = {
  'name': 'Question 20_white_outcomes_counts',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'white_outcomes_counts'
          >>> 'white_outcomes_counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'white_outcomes_counts'
          >>> # from its initial state (of ...)
          >>> white_outcomes_counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # white_outcomes_counts should be a Pandas Series
          >>> isinstance(white_outcomes_counts, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
