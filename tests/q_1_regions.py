test = {
  'name': 'Question 1_regions',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'regions'
          >>> 'regions' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'regions'
          >>> # from its initial state (of ...)
          >>> regions is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # regions should be a Pandas Series
          >>> isinstance(regions, pd.Series)
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
