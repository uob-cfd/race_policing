test = {
  'name': 'Question 15_outcomes',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'outcomes'
          >>> 'outcomes' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'outcomes'
          >>> # from its initial state (of ...)
          >>> outcomes is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Does your result come from the valid_eth_outcome
          >>> # data frame?
          >>> len(outcomes) == len(valid_eth_outcome)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # outcomes should be a Pandas Series
          >>> isinstance(outcomes, pd.Series)
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
