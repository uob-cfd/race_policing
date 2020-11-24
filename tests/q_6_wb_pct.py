test = {
  'name': 'Question 6_wb_pct',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'white_british_pct'
          >>> 'white_british_pct' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Not yet!
          >>> # But - don't forget - you can't just type in the number here.
          >>> np.isclose(float(white_british_pct), 79.2)
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
