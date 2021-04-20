from gym.envs.registration import register

register(
    id='cryptotrade-v0',
    entry_point='gym_foo.envs:newCryptoEnv',
    kwargs={
        'window_size': 24,
        'frame_bound': (24, len(datasets.FOREX_EURUSD_1H_ASK))
    }
)
