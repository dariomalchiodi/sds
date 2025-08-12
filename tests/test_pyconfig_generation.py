import unittest
import sys
import os

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from code.sds import process_myst_document, _extract_imports

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
        """Test that micropip installation is generated when imports are present."""
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
        
        # Current implementation uses micropip for dynamic package installation
        # instead of py-config static configuration
        self.assertIn('micropip.install("altair")', result)
        
        # Check that PyScript setup is present
        self.assertIn('<py-script>', result)
        self.assertIn('import micropip', result)
        
        # Should include matplotlib setup
        self.assertIn('import matplotlib', result)
        
        # Verify that the document is processed correctly with Python blocks
        self.assertIn('```python', result)
        self.assertIn('</py-script>', result)
    
    def test_process_myst_document_no_imports(self):
        """Test PyScript setup when there are no custom imports."""
        myst_content = '''# Test Document

```python
x = 5
y = x * 2
```
'''
        
        result = process_myst_document(myst_content, include_setup=True)
        
        # Standard libraries are always included in PyScript setup
        self.assertIn('micropip.install("altair")', result)
        self.assertIn('import pandas as pd', result)
        self.assertIn('import matplotlib', result)
        
        # PyScript should be present
        self.assertIn('<py-script>', result)
        
        # Should include the Python code block
        self.assertIn('x = 5', result)
        self.assertIn('y = x * 2', result)

if __name__ == '__main__':
    unittest.main()
