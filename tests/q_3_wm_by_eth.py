test = {
  'name': 'Question 3_wm_by_eth',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'west_midlands_by_eth'
          >>> 'west_midlands_by_eth' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # west_midlands_by_eth should be have same number of rows as
          >>> # there are True values in is_wm
          >>> len(west_midlands_by_eth) == np.count_nonzero(is_west_midlands)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # west_midlands_by_eth should be a data frame.
          >>> isinstance(west_midlands_by_eth, pd.DataFrame)
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
