test = {
  'name': 'Question 8_ethnicity',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ethnicity'
          >>> 'ethnicity' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # ethnicity should be have same number of rows as
          >>> # the data frame.
          >>> len(ethnicity) == len(stop_search)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # ethnicity should be a Pandas series
          >>> isinstance(ethnicity, pd.Series)
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
