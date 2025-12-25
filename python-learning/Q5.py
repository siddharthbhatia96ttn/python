class UserRepository:
    def __init__(self, users):
        # Simulating a large dataset (could be millions of records)
        self._users = users

    def stream_active_users(self):
        """
        Generator method that lazily yields active users.
        """
        for user in self._users:
            if user["active"]:
                yield user


# ------------------ Usage Demonstration ------------------

if __name__ == "__main__":

    # Simulated large dataset
    users_data = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Charlie", "active": True},
        {"id": 4, "name": "David", "active": True},
        {"id": 5, "name": "Eva", "active": False},
    ]

    repo = UserRepository(users_data)

    # Get generator (no data processed yet)
    user_stream = repo.stream_active_users()

    # Partial consumption
    print(next(user_stream))   # First active user
    print(next(user_stream))   # Second active user

    # Resume iteration later
    for user in user_stream:
        print(user)
