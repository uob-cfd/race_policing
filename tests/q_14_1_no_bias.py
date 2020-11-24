test = {
  'name': 'Question 14_1_no_bias',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'likely_no_bias'
          >>> 'likely_no_bias' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'likely_no_bias'
          >>> # from its initial state (of ...)
          >>> likely_no_bias is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 1 <= likely_no_bias <= 5
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
