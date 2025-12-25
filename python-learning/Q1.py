class User:
    # Class-level attribute to track total active users
    total_active_users = 0

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.active = True

        User.total_active_users += 1

    def get_role(self):
        return "Generic User"

    def get_permissions(self):
        return ["read"]

    def deactivate(self):
        if self.active:
            self.active = False
            User.total_active_users -= 1

    @classmethod
    def get_total_active_users(cls):
        return cls.total_active_users


# ------------------ Subclasses ------------------

class AdminUser(User):
    def get_role(self):
        return "Admin"

    def get_permissions(self):
        return ["read", "write", "delete", "manage_users"]


class StaffUser(User):
    def get_role(self):
        return "Staff"

    def get_permissions(self):
        return ["read", "write"]


class CustomerUser(User):
    def get_role(self):
        return "Customer"

    def get_permissions(self):
        return ["read", "purchase"]


# ------------------ Main Execution ------------------

if __name__ == "__main__":
    admin = AdminUser(1, "Alice", "alice@company.com")
    staff = StaffUser(2, "Bob", "bob@company.com")
    customer = CustomerUser(3, "Charlie", "charlie@gmail.com")

    print(admin.get_role(), admin.get_permissions())
    print(staff.get_role(), staff.get_permissions())
    print(customer.get_role(), customer.get_permissions())

    print("Total active users:", User.get_total_active_users())

    customer.deactivate()
    print("Total active users after deactivation:", User.get_total_active_users())
