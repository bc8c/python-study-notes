import sys
import platform

print("🎉 Python environment test successful!")
print(f"Python version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")
print("Virtual environment:", sys.prefix)
