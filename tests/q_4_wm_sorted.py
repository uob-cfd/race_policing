test = {
  'name': 'Question 4_wm_sorted',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'west_midlands_sorted'
          >>> 'west_midlands_sorted' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # west_midlands_sorted should be have same number of rows as
          >>> # there are True values in is_wm
          >>> len(west_midlands_sorted) == np.count_nonzero(is_west_midlands)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # west_midlands_sorted should be a data frame.
          >>> isinstance(west_midlands_sorted, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # west_midlands_sorted first value for percent should be largest
          >>> # percent value.  Are the values sorted in descending order?
          >>> west_midlands_sorted['%'].iat[0] == west_midlands_sorted['%'].max()
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
