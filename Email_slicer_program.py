def main():
        print("Welcome to Ballershopke Email Slicer")
        print("")


        email_input = input("Input your email address")


        (username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")


        print("Username : ", username)
        print("Domain : ", domain)
        print("Extension : ", extension)






main()