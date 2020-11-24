test = {
  'name': 'Question 19_white_outcomes',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'white_outcomes'
          >>> 'white_outcomes' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # white_outcomes should have same number of values as there
          >>> # are White British in 'recoded_eth' column.
          >>> rce = valid_eth_outcome['recoded_eth']
          >>> n_white = np.count_nonzero(rce == 'White British')
          >>> len(white_outcomes) == n_white
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # white_outcomes should be a Series
          >>> isinstance(white_outcomes, pd.Series)
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
