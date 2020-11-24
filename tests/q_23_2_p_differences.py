test = {
  'name': 'Question 24_2_p_differences',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_differences'
          >>> 'p_differences' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_differences'
          >>> # from its initial state (of ...)
          >>> p_differences is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_differences should have 10000 elements
          >>> len(p_differences)
          10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # p_differences should be a difference in proportion.
          >>> np.all(np.logical_and(p_differences >= -1, p_differences <= 1))
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
