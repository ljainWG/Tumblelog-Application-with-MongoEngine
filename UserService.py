from datetime import datetime
from User import User

class UserService:
    def create_user(self, first_name, last_name, email, gender, password, dob):
        """Create a new user in the database."""
        try:
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                gender=gender,
                password=password,
                dob=dob
            )
            user.save()
            return f"User {first_name} {last_name} created successfully."
        except Exception as e:
            return f"Error creating user: {e}"

    def get_user_by_email(self, email):
        """Retrieve a user by email."""
        try:
            user = User.objects(email=email).first()
            return user if user else "User not found."
        except Exception as e:
            return f"Error fetching user: {e}"

    def update_user(self, email, update_data):
        """Update user details by email."""
        try:
            user = User.objects(email=email).first()
            if not user:
                return "User not found."

            user.update(**update_data)
            return f"User {email} updated successfully."
        except Exception as e:
            return f"Error updating user: {e}"

    def delete_user(self, email):
        """Delete a user by email."""
        try:
            user = User.objects(email=email).first()
            if not user:
                return "User not found."

            user.delete()
            return f"User {email} deleted successfully."
        except Exception as e:
            return f"Error deleting user: {e}"
