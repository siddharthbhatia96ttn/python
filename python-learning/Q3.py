class User:
    def __init__(self, user_id, name, role, permissions):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.permissions = permissions

    # ------------------ Human-readable ------------------
    def __str__(self):
        return f"{self.name} ({self.role})"

    # ------------------ Debug representation ------------------
    def __repr__(self):
        return (
            f"User(user_id={self.user_id}, "
            f"name='{self.name}', "
            f"role='{self.role}', "
            f"permissions={self.permissions})"
        )

    # ------------------ Business metric ------------------
    def __len__(self):
        return len(self.permissions)

    # ------------------ Equality ------------------
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    # ------------------ Ordering ------------------
    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return len(self.permissions) < len(other.permissions)

    # ------------------ Callable behavior ------------------
    def __call__(self, action):
        if action in self.permissions:
            return f"{self.name} executed '{action}'"
        return f"Access denied for '{action}'"


# ------------------ Usage Demonstration ------------------

if __name__ == "__main__":
    admin = User(
        1,
        "Alice",
        "Admin",
        ["read", "write", "delete", "manage"]
    )

    staff = User(
        2,
        "Bob",
        "Staff",
        ["read", "write"]
    )

    # __str__
    print(str(admin))     # Alice (Admin)

    # __repr__
    print(repr(admin))

    # __len__
    print("Admin permission count:", len(admin))

    # __eq__
    print(admin == staff)     # False
    print(admin == User(1, "Alice Clone", "Admin", []))  # True

    # __lt__
    print(staff < admin)      # True

    # __call__
    print(admin("delete"))
    print(staff("delete"))
