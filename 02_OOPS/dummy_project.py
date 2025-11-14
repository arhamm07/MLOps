class Chatbook():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook
                            1.Register
                            2.Login
                            3.Write a post
                            4.Message a Friend
                            5.Exit""")
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.message_friend()
        elif user_input == "5":
            exit()

    def register(self):
        email = input('Enter your Email: ')
        password = input('Enter your Password: ')
        self.username = email
        self.password = password

        print('Registration Successful')
        print('\n')
        self.menu()

    def login(self):
        email = input('Enter your Email: ')
        password = input('Enter your Password: ')

        if email == self.username and password == self.password:
            self.loggedIn = True
            print('Login Successful')
            print('\n')
            self.menu()
        else:
            print('Invalid Email or Password or Try to Register First')
            print('\n')
            self.menu()

    def write_post(self):
        if self.loggedIn:
            post = input('Enter your Post: ')
            print('Post Successful')
            print('\n')
            self.menu()
        else:
            print('Please Login First')
            print('\n')
            self.menu()

    def message_friend(self):
        if self.loggedIn:
            friend = input('Enter your Friend Email: ')
            message = input('Enter your Message: ')
            print('Message Successful')
            print('\n')
            self.menu()
        else:
            print('Please Login First')
            print('\n')
            self.menu()

obj = Chatbook()