import unittest
import sys
import os

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from sds import _extract_imports, process_myst_document

class TestPyConfigGeneration(unittest.TestCase):
    
    def test_extract_imports_simple(self):
        """Test basic import extraction."""
        code = """
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
"""
        imports = _extract_imports(code)
        expected = {'numpy', 'pandas', 'matplotlib'}
        self.assertEqual(imports, expected)
    
    def test_extract_imports_builtin_filtered(self):
        """Test that built-in modules are filtered out."""
        code = """
import sys
import os
import numpy as np
import json
from io import StringIO
"""
        imports = _extract_imports(code)
        expected = {'numpy'}  # sys, os, json, io should be filtered out
        self.assertEqual(imports, expected)
    
    def test_extract_imports_complex(self):
        """Test extraction with complex import patterns."""
        code = """
import numpy.random as npr
from scipy.stats import norm
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
"""
        imports = _extract_imports(code)
        expected = {'numpy', 'scipy', 'matplotlib', 'pandas'}
        self.assertEqual(imports, expected)
    
    def test_process_myst_document_with_pyconfig(self):
        """Test that py-config is generated when imports are present."""
        myst_content = '''# Test Document

```python
import numpy as np
import pandas as pd
x = np.array([1, 2, 3])
```

Some text.

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```
'''
        
        result = process_myst_document(myst_content, include_setup=True)
        
        # Check that py-config tag is present
        self.assertIn('<py-config', result)
        self.assertIn('"packages":', result)
        
        # Check that the expected packages are included
        self.assertIn('"matplotlib"', result)
        self.assertIn('"numpy"', result)
        self.assertIn('"pandas"', result)
        
        # Check that py-config comes before py-script tags
        py_config_pos = result.find('<py-config')
        py_script_pos = result.find('<py-script>')
        self.assertLess(py_config_pos, py_script_pos)
    
    def test_process_myst_document_no_imports(self):
        """Test that no py-config is generated when there are no imports."""
        myst_content = '''# Test Document

```python
x = 5
y = x * 2
```
'''
        
        result = process_myst_document(myst_content, include_setup=True)
        
        # Check that py-config tag is not present
        self.assertNotIn('<py-config', result)
        
        # But py-script should still be present
        self.assertIn('<py-script>', result)

if __name__ == '__main__':
    unittest.main()
