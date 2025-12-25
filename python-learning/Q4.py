import time
import functools


# ------------------ Simple Logging Decorator ------------------
def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(
            f"[LOG] Function: {func.__name__} | "
            f"Execution Time: {end_time - start_time:.4f}s"
        )
        return result

    return wrapper


# ------------------ Parameterized Decorator ------------------
def conditional_logger(enable_logging=True):
    def decorator(func):
        if not enable_logging:
            return func  # No wrapping if logging disabled

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Calling {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# ------------------ Class Using Decorators ------------------
class UserService:

    @log_execution
    def create_user(self, name):
        time.sleep(0.1)
        return f"User '{name}' created"

    @conditional_logger(enable_logging=True)
    def delete_user(self, name):
        time.sleep(0.05)
        return f"User '{name}' deleted"

    @conditional_logger(enable_logging=False)
    def get_user(self, name):
        time.sleep(0.02)
        return f"User '{name}' fetched"


# ------------------ Usage Demonstration ------------------
if __name__ == "__main__":
    service = UserService()

    print(service.create_user("Alice"))
    print(service.delete_user("Bob"))
    print(service.get_user("Charlie"))
