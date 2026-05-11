import unittest
from sds.sds import process_myst_document, _extract_imports


class TestExtractImports(unittest.TestCase):
    def test_simple(self):
        code = """
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
"""
        self.assertEqual(_extract_imports(code), {'numpy', 'pandas', 'matplotlib'})

    def test_builtins_filtered(self):
        code = """
import sys
import os
import numpy as np
import json
from io import StringIO
"""
        self.assertEqual(_extract_imports(code), {'numpy'})

    def test_complex_patterns(self):
        code = """
import numpy.random as npr
from scipy.stats import norm
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
"""
        self.assertEqual(_extract_imports(code), {'numpy', 'scipy', 'matplotlib', 'pandas'})


class TestProcessMystDocumentImports(unittest.TestCase):
    def test_with_imports(self):
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

        self.assertIn('<script type="py">', result)
        self.assertIn('import matplotlib', result)
        self.assertIn('```python', result)

    def test_no_imports(self):
        myst_content = '''# Test Document

```python
x = 5
y = x * 2
```
'''
        result = process_myst_document(myst_content, include_setup=True)

        self.assertIn('<script type="py">', result)
        self.assertIn('import matplotlib', result)
        self.assertIn('x = 5', result)
        self.assertIn('y = x * 2', result)


if __name__ == '__main__':
    unittest.main()
