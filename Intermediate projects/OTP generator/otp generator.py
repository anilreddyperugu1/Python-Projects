import random

otp = random.randint(1111, 9999)
print("Your OTP would be: ", otp)
OTP = int(input("Enter the OTP: "))

if otp == OTP:
    print("OTP verified successfully")
else:
    print("OTP doesn't match! please try again.")

