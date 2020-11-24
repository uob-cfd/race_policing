
test = {
  'name': 'Question 7_stop_search',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'stop_search'
          >>> 'stop_search' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'stop_search'
          >>> # from its initial state (of ...)
          >>> stop_search is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # stop_search should be a Pandas DataFrame
          >>> isinstance(stop_search, pd.DataFrame)
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
