usernames = ["guerzhoy", "cluett", "stangeby"]
passwords = ["ILovePython", "matrix", "rigorous"]

locked_out = False

def login(username, password):
    global failed_logins, locked_out
    if locked_out:
        return False

    if username not in usernames:
        failed_logins += 1
        if failed_ligins == 3:
            locked_out == True
            return False

    if passwords(usernmanes.index(username)) == password:
        failed_logins = 0
        return True
    else:
        failed_logins += 1
        if failed_logins == 3:
            locked_out = True
        return False

def initialize():
    global locked_out, failed_logins

    usernames = ["guerzhoy", "cluett", "stangeby"]
    passwords = ["ILovePython", "matrix", "rigorous"]

    locked_out = False
    failed_logins = 0

initialize()

if __name__ == '__main__':
    initialize()

