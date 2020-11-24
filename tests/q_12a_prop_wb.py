test = {
  'name': 'Question 12a_prop_wb',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'prop_wb'
          >>> 'prop_wb' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You need to change the value from the default ...
          >>> prop_wb is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # prop_wb should between 0 and 1
          >>> 0 <= prop_wb <= 1
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
