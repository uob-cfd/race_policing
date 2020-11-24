test = {
  'name': 'Question 9_outcomes_counts',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'outcomes_counts'
          >>> 'outcomes_counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'outcomes_counts'
          >>> # from its initial state (of ...)
          >>> outcomes_counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # outcomes_counts should be a Pandas Series
          >>> isinstance(outcomes_counts, pd.Series)
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
