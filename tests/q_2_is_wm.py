test = {
  'name': 'Question 2_is_wm',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'is_west_midlands'
          >>> 'is_west_midlands' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_west_midlands should be have same number of rows as data frame
          >>> len(is_west_midlands) == len(regions_by_eth)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is_west_midlands should be Boolean -
          >>> # it should have only True and False values.
          >>> set(is_west_midlands) == {True, False}
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
