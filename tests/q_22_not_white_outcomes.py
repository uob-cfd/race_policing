test = {
  'name': 'Question 22_not_white_outcomes',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'not_white_outcomes'
          >>> 'not_white_outcomes' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # not_white_outcomes should have fewer rows than the
          >>> # data frame
          >>> len(not_white_outcomes) < len(valid_eth_outcome)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # not_white_outcomes should be a Series
          >>> isinstance(not_white_outcomes, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
