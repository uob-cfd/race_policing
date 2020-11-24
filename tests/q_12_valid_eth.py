test = {
  'name': 'Question 12_n_valid_eth',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'valid_eth_outcome'
          >>> 'valid_eth_outcome' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'valid_eth_outcome'
          >>> # from its initial state (of ...)
          >>> valid_eth_outcome is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # recoded_eth_counts should be a Pandas DataFrame
          >>> isinstance(valid_eth_outcome, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # No missing values in 'recoded_eth' column.
          >>> np.all(valid_eth_outcome['recoded_eth'].notna())
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
