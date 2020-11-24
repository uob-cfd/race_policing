test = {
  'name': 'Question 20_white_arrested_p',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'white_arrested_p'
          >>> 'white_arrested_p' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'white_arrested_p'
          >>> # from its initial state (of ...)
          >>> white_arrested_p is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # white_arrested_p should be a proportion
          >>> 0 <= white_arrested_p <= 1
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
