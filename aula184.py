from dotenv import load_dotenv
import os
load_dotenv()

print(os.getenv("USER_BD"))
print(os.getenv("PASS_BD"))
print(os.getenv("HOST_BD"))