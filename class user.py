class User:
    """Class of user stores a tipical user info"""

    def __init__(self, first_name, last_name, username, location, email, middle_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.username = username
        self.location = location
        self.email = email
        self.login_attempts = 0

    def full_name(self):
        if self.middle_name == '':
            entire_name = self.first_name + ' ' + self.last_name
        else:
            entire_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        return entire_name.title()

    # long_name = str(self.year) + ' ' + self.make + ' ' + self.model

    def describe_user(self):
        """returns full name e-mail, username and location of any given user"""
        print(f'the user: {self.username} name is {self.full_name()},'
              f' his location and e-mail are respectively {self.location}, {self.email}.')

    def greet_user(self):
        """simple custom user greeting"""
        print(f'Welcome back {self.username}. ')

    def increment_login_attempts ( self ) :
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts ( self ) :
        """Reset login_attempts to 0."""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

yann = User('yann', 'moskovitz', 'sefyammas', 'yann.moskovitz@example.com.br', 'brazil', middle_name='comparato')
yann.describe_user()
yann.greet_user()

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))