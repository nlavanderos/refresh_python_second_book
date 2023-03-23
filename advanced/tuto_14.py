#obtain data from .env local file
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
import os
print(os.getenv("PSSWRD_PYPY_TEST"))