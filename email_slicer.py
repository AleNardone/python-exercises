f = open("email_slicer.txt", "w")
email = input("Enter your email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
f.write(f"Your username is '{username}' and your domian is '{domain}'")
print(f"Your username is '{username}' and your domian is '{domain}'")
f.close()




