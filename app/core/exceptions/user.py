class UsersNotFound(Exception):
    """Exception raised when a user is not found in the database."""

    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} not found.")


class UserAlreadyExists(Exception):
    """Exception raised when a user already exists in the database."""

    def __init__(self, username: str):
        self.username = username
        super().__init__(f"User with username '{username}' already exists.")


class InvalidUserInput(Exception):
    """Exception raised when the user input is invalid."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Invalid user input: {message}")


class InvalidUserData(Exception):
    """Exception raised when the user data provided is invalid."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Invalid user data: {message}")
