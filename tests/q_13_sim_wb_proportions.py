test = {
  'name': 'Question 13_sim_wb_proportions',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'sim_wb_proportions'
          >>> 'sim_wb_proportions' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'sim_wb_proportions'
          >>> # from its initial state (of ...)
          >>> sim_wb_proportions is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # sim_wb_proportions should have 10000 elements
          >>> len(sim_wb_proportions)
          10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          # np.random.binomial(1885, 0.792, 10000000) / n_valid_eth
          'code': r"""
          >>> # At least some of your values are suprisingly low.
          >>> np.all(sim_wb_proportions > 0.5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # At least some of your values are suprisingly high.
          >>> np.all(sim_wb_proportions < 1)
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
