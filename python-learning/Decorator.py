
import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Start Time: {start_time}")

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"End Time: {end_time}")

        print(f"Total Time Taken: {end_time - start_time} seconds")
        return result
    return wrapper

@calculate_time
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers

# Call the function
append_numbers()


import time

def retry(retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < retries:
                        time.sleep(1)  # optional delay between retries
            raise last_exception
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")
    raise ValueError("Something went wrong")

# Call the function
may_fail("Siddharth")

#Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


# Example usage
print(square_root(16))   # Output: 4.0
print(square_root(9))    # Output: 3.0

# This will raise an error
print(square_root(-4))

# Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
def requires_permission(func):
    def wrapper(user, user_id):
        if 'admin' in user.get('permissions', []):
            return func(user, user_id)
        else:
            print("Access denied")
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


# Users
user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}


# Test calls
delete_user(user1, 101)   # Allowed
delete_user(user2, 102)   # Access denied
delete_user(user3, 103)   # Access denied