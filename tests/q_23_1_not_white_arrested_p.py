test = {
  'name': 'Question 20_not_white_arrested_p',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'not_white_arrested_p'
          >>> 'not_white_arrested_p' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'not_white_arrested_p'
          >>> # from its initial state (of ...)
          >>> not_white_arrested_p is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # not_white_arrested_p should be a proportion
          >>> 0 <= not_white_arrested_p <= 1
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
