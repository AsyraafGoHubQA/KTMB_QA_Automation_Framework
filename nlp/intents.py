INTENTS = {

    "login": [
        "login",
        "log in",
        "sign in",
        "authenticate"
    ],

    "search": [
        "search",
        "find",
        "look for"
    ],

    "booking": [
        "book",
        "booking",
        "reserve"
    ],

    "payment": [
        "payment",
        "pay"
    ]
}


SCENARIOS = {

    "valid": [
        "valid account",
        "correct account",
        "correct credentials",
        "successful login",
        "valid login",

        # NEW
        "valid credentials",
        "login with valid credentials",
        "login using valid credentials",
        "login successfully",
        "login with valid account",
        "correct username and password",
        "valid username and password"
    ],

    "invalid_password": [
        "invalid password",
        "wrong password",
        "incorrect password",
        "bad password",

        # NEW
        "login with wrong password",
        "login using wrong password"
    ],

    "invalid_username": [
        "invalid username",
        "wrong username",
        "incorrect username",

        # NEW
        "login with wrong username",
        "login using wrong username"
    ],

    "empty_username": [
        "empty username",
        "blank username",
        "without username",

        # NEW
        "login without username"
    ],

    "empty_password": [
        "empty password",
        "blank password",
        "without password",

        # NEW
        "login without password"
    ]
}