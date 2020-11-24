test = {
  'name': 'Question 9_eth_counts',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'eth_counts'
          >>> 'eth_counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'eth_counts'
          >>> # from its initial state (of ...)
          >>> eth_counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # eth_counts should be a Pandas Series
          >>> isinstance(eth_counts, pd.Series)
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
