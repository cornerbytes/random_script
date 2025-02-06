#!/usr/bin/python3 
import bcrypt


if __name__ == "__main__":
    PW = input("enter pass: ").encode()
    print(f"bcrypt: {bcrypt.hashpw(PW, bcrypt.gensalt()).decode()}")
