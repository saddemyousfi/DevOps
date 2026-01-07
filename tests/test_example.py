import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add

def test_basic_math():
    assert 1 + 1 == 3   # ❌ deliberate failure
