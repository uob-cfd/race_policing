test = {
  'name': 'Question 24_outcome_same',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'likely_outcome_same'
          >>> 'likely_outcome_same' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'likely_outcome_same'
          >>> # from its initial state (of ...)
          >>> likely_outcome_same is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 1 <= likely_outcome_same <= 5
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
