class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    # ------------------ Class Method ------------------
    @classmethod
    def from_string(cls, data_str):
        """
        Creates a User object from a serialized string.
        Format: "id,name,email"
        """
        user_id, name, email = data_str.split(",")

        # Reuse static validation
        if not cls.is_valid_email(email):
            raise ValueError("Invalid email format")

        return cls(int(user_id), name.strip(), email.strip())

    # ------------------ Static Method ------------------
    @staticmethod
    def is_valid_email(email):
        """
        Validates email format.
        Independent of class or instance state.
        """
        return "@" in email and "." in email


# ------------------ Usage Demonstration ------------------

if __name__ == "__main__":

    # Using static method (no object needed)
    print(User.is_valid_email("test@gmail.com"))   # True
    print(User.is_valid_email("invalid-email"))    # False

    # Using class method to create object
    user_data = "101, Alice, alice@gmail.com"
    user = User.from_string(user_data)

    print(user.user_id)
    print(user.name)
    print(user.email)
