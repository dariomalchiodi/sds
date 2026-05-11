import unittest
from sds.sds import process_myst_document


class TestProcessMystDocument(unittest.TestCase):

    def test_single_python_block(self):
        myst_content = '''# My Document

Here is some Python code:

```python
x = 10
y = 20
x + y
```

And here is some more text.
'''
        result = process_myst_document(myst_content)

        # Original prose and code block are preserved
        self.assertIn('# My Document', result)
        self.assertIn('Here is some Python code:', result)
        self.assertIn('And here is some more text.', result)
        self.assertIn('```python\nx = 10\ny = 20\nx + y\n```', result)

        # A single PyScript block is appended at the end
        self.assertIn('<script type="py">', result)
        self.assertIn('x = 10', result)
        self.assertIn('y = 20', result)
        self.assertIn('result = x + y', result)
        self.assertIn('</script>', result)

        # PyScript block comes after the prose
        text_pos = result.find('And here is some more text.')
        script_pos = result.find('<script type="py">')
        self.assertLess(text_pos, script_pos)

    def test_multiple_python_blocks(self):
        myst_content = '''# Document

```python
a = 5
```

Some text between blocks.

```python
b = 10
a + b
```
'''
        result = process_myst_document(myst_content, include_setup=False)

        # All cells are combined into one PyScript block
        self.assertEqual(result.count('<script type="py">'), 1)
        self.assertEqual(result.count('</script>'), 1)

        # Both code blocks appear in the output
        self.assertIn('a = 5', result)
        self.assertIn('result = a + b', result)

        # PyScript block comes after both code blocks
        last_python_block = result.rfind('```python')
        script_pos = result.find('<script type="py">')
        self.assertLess(last_python_block, script_pos)

    def test_inline_python_role(self):
        myst_content = '''# Document

Here is an inline role: {py}`x = 42` and some more text.
'''
        result = process_myst_document(myst_content)

        # Inline role is replaced with a span placeholder
        self.assertNotIn('{py}`x = 42`', result)
        self.assertIn('<span id="inline-1" class="py-inline-splash">', result)

        # The expression appears inside the appended script block
        self.assertIn('x = 42', result)

    def test_no_python_blocks(self):
        myst_content = '''# Document

This document has no Python code.

```javascript
console.log("Hello");
```

Just some regular text.
'''
        result = process_myst_document(myst_content)

        self.assertEqual(result, myst_content)
        self.assertNotIn('```{raw} html', result)
        self.assertNotIn('<script type="py">', result)

    def test_mixed_content(self):
        myst_content = '''# Mixed Document

```python
import math
radius = 5
```

Some explanation here.

```python
area = math.pi * radius ** 2
area
```

And inline: {py}`print("Hello")`

```python
x = [1, 2, 3]
sum(x)
```
'''
        result = process_myst_document(myst_content, include_setup=False)

        # Inline span for cell 3 (cells 1, 2 are code blocks, 3 is inline, 4 is last block)
        self.assertIn('<span id="inline-3" class="py-inline-splash">', result)

        # Original prose preserved
        self.assertIn('# Mixed Document', result)
        self.assertIn('Some explanation here.', result)
        self.assertIn('And inline:', result)

        # One combined PyScript block at the end
        self.assertEqual(result.count('<script type="py">'), 1)

    def test_assignment_only_block(self):
        myst_content = '''# Document

```python
x = 42
y = x * 2
```
'''
        result = process_myst_document(myst_content)

        # Code appears in the PyScript block
        self.assertIn('x = 42', result)

        # No result-capture try block since there is no final expression
        self.assertNotIn('try:\n        result =', result)

    def test_with_setup_disabled(self):
        myst_content = '''# Document

```python
x = 42
```
'''
        result = process_myst_document(myst_content, include_setup=False)

        # Setup snippet content is absent
        self.assertNotIn('PyScript utilities loaded successfully', result)
        self.assertNotIn('_ensure_localfs', result)

        # Code block and PyScript wrapper are still present
        self.assertIn('```python', result)
        self.assertIn('<script type="py">', result)

    def test_with_setup_enabled(self):
        myst_content = '''# Document

```python
x = 42
```
'''
        result = process_myst_document(myst_content, include_setup=True)

        # Setup snippet content is present
        self.assertIn('PyScript utilities loaded successfully', result)
        self.assertIn('from pyscript import display', result)
        self.assertIn('_ensure_localfs', result)

        # Setup appears after the code block
        python_block_pos = result.find('```python')
        setup_pos = result.find('PyScript utilities loaded successfully')
        self.assertLess(python_block_pos, setup_pos)


if __name__ == '__main__':
    unittest.main()
