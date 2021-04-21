from gym.envs.registration import register

register(
    id='cryptotrade-v0',
    entry_point='new_CustomTrader.envs:CryptoEnv',
    kwargs={
        'window_size': 24,
        'frame_bound': (24, 250)
    }
)
