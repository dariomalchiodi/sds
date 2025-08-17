import unittest
from sds.sds import extract_python_roles

class TestExtractPythonRoles(unittest.TestCase):
    def test_simple_code_block(self):
        source = '''
Some text
```python
x = 1
y = 2
```
More text
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [('x = 1\ny = 2', None, False)])

    def test_myst_style_block(self):
        source = '''
Some text
```{python}
def hello():
    print("Hello")
```
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [('def hello():\n    print("Hello")', None, False)])

    def test_multiple_blocks(self):
        source = '''
```python
x = 1
```
Some text
```python
y = 2
```
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [('x = 1', None, False), ('y = 2', None, False)])

    def test_empty_block(self):
        source = '''
```python
```
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [('', None, False)])

    def test_no_python_blocks(self):
        source = '''
```javascript
var x = 1;
```
Some text
```
plain text
```
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [])

    def test_inline_python_role(self):
        source = 'Some text with `x = 42`{py} inline code'
        result = extract_python_roles(source)
        self.assertEqual(result, [('x = 42', None, True)])

    def test_multiple_inline_roles(self):
        source = '''
This is `x = 1`{py} and this is `y = 2`{py}
More text with `print("Hello")`{py}
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [('x = 1', None, True), ('y = 2', None, True), ('print("Hello")', None, True)])

    def test_mixed_blocks_and_roles(self):
        source = '''
Here is an inline role `x = 1`{py}
And here is a code block:
```python
y = 2
z = 3
```
And another inline role `print(x)`{py}
'''
        result = extract_python_roles(source)
        self.assertEqual(result, [('x = 1', None, True), ('y = 2\nz = 3', None, False), ('print(x)', None, True)])

if __name__ == '__main__':
    unittest.main()
