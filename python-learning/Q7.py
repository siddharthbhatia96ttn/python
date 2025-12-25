class UserValidator:
    def __init__(self, users):
        self.users = users

    def validate_user_id(self, user_id):
        """
        Checks if a user ID exists.
        Uses loop-else instead of flags.
        """
        for user in self.users:
            if user["id"] == user_id:
                print(f"User found: {user}")
                break
        else:
            # Executes only if no break occurred
            print(f"User with ID {user_id} not found")


# ------------------ Usage Demonstration ------------------

if __name__ == "__main__":

    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]

    validator = UserValidator(users)

    validator.validate_user_id(2)   # Found → else skipped
    validator.validate_user_id(99)  # Not found → else executed
