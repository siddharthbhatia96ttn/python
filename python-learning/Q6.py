from collections import namedtuple

# ------------------ Immutable Configuration ------------------
AppConfig = namedtuple(
    "AppConfig",
    ["app_name", "version", "max_users"]
)


# ------------------ Class Using Immutable Config ------------------
class Application:
    def __init__(self, config: AppConfig):
        self._config = config

    def get_config(self):
        return self._config

    def display_config(self):
        print(
            f"App: {self._config.app_name}, "
            f"Version: {self._config.version}, "
            f"Max Users: {self._config.max_users}"
        )


# ------------------ Usage Demonstration ------------------
if __name__ == "__main__":

    # Create immutable config
    config = AppConfig(
        app_name="UserManagementSystem",
        version="1.0.0",
        max_users=1000
    )

    app = Application(config)
    app.display_config()

    # Retrieve config safely
    retrieved_config = app.get_config()
    print(retrieved_config)

    # ------------------ Immutability Demonstration ------------------
    try:
        # This will FAIL because namedtuple is immutable
        retrieved_config.max_users = 5000
    except AttributeError as e:
        print("Immutability enforced:", e)

    # Original config remains unchanged
    app.display_config()
