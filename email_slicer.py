f = open("email_slicer.txt", "w")
email = input("Enter your email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@'):]
f.write(f"Your username is '{username}' and your domain is '{domain}'")
print(f"Your username is '{username}' and your domain is '{domain}'")
f.close()




