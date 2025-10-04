from stores.TokensStore import TokensStore


class MainStore:
    def __init__(self):
        self.tokens = TokensStore()
