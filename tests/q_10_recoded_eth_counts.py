test = {
  'name': 'Question 10_recoded_eth_counts',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'recoded_eth_counts'
          >>> 'recoded_eth_counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'recoded_eth_counts'
          >>> # from its initial state (of ...)
          >>> recoded_eth_counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # recoded_eth_counts should be a Pandas Series
          >>> isinstance(recoded_eth_counts, pd.Series)
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
