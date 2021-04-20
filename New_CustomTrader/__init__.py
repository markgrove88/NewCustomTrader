from gym.envs.registration import register

register(
    id='cryptotrade-v0',
    entry_point='New_CustomTrader.envs:newCryptoEnv',
    kwargs={
        'window_size': 24,
        'frame_bound': (24, 250)
    }
)
