import os
import sys

project_root = os.path.join(os.path.dirname(__file__), '..')
print("Project Root Directory:", project_root)
sys.path.insert(0, project_root)
print("Updated sys.path:", sys.path)