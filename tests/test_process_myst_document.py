import unittest
from code.sds import process_myst_document

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
        
        # Should contain original content
        self.assertIn("# My Document", result)
        self.assertIn("Here is some Python code:", result)
        self.assertIn("And here is some more text.", result)
        
        # Should contain the original Python block
        self.assertIn("```python\nx = 10\ny = 20\nx + y\n```", result)
        
        # Should contain the HTML divs
        self.assertIn('<div id="out-1" class="cell-out"></div>', result)
        self.assertIn('<div id="stdout-1" class="cell-stdout"></div>', result)
        self.assertIn('<div id="stderr-1" class="cell-stderr"></div>', result)
        self.assertIn('<div id="graph-1" class="cell-graph no-mathjax"></div>', result)
        
        # Should contain PyScript at the end
        self.assertIn("<py-script>", result)
        self.assertIn("x = 10", result)
        self.assertIn("y = 20", result)
        self.assertIn("result = x + y", result)
        self.assertIn("</py-script>", result)
        
        # PyScript should be at the end - after "And here is some more text."
        text_pos = result.find("And here is some more text.")
        pyscript_pos = result.find("<py-script>")
        self.assertLess(text_pos, pyscript_pos)
    
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
        
        # Should have two sets of HTML divs with different IDs
        self.assertIn('<div id="out-1" class="cell-out"></div>', result)
        self.assertIn('<div id="out-2" class="cell-out"></div>', result)
        self.assertIn('<div id="stdout-1" class="cell-stdout"></div>', result)
        self.assertIn('<div id="stdout-2" class="cell-stdout"></div>', result)
        self.assertIn('<div id="graph-1" class="cell-graph no-mathjax"></div>', result)
        self.assertIn('<div id="graph-2" class="cell-graph no-mathjax"></div>', result)
        
        # Should have 2 PyScript blocks for the 2 code blocks (at the end)
        self.assertEqual(result.count("<py-script>"), 2)
        self.assertEqual(result.count("</py-script>"), 2)
        
        # PyScript should be at the end
        last_python_block = result.rfind("```python")
        first_pyscript = result.find("<py-script>")
        self.assertLess(last_python_block, first_pyscript)
    
    def test_inline_python_role(self):
        myst_content = '''# Document

Here is an inline role: `x = 42`{py} and some more text.
'''
        result = process_myst_document(myst_content)
        
        # Should NOT contain original inline role (it gets replaced)
        self.assertNotIn("`x = 42`{py}", result)
        
        # Should contain inline span element for the inline role
        self.assertIn('<span id="inline-1" class="py-inline-result">', result)
        
        # Should contain PyScript execution code for the inline expression
        self.assertIn("x = 42", result)
    
    def test_no_python_blocks(self):
        myst_content = '''# Document

This document has no Python code.

```javascript
console.log("Hello");
```

Just some regular text.
'''
        result = process_myst_document(myst_content)
        
        # Should return unchanged content
        self.assertEqual(result, myst_content)
        
        # Should not contain any HTML blocks
        self.assertNotIn("```{raw} html", result)
        self.assertNotIn("<py-script>", result)
    
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

And inline: `print("Hello")`{py}

```python
x = [1, 2, 3]
sum(x)
```
'''
        result = process_myst_document(myst_content, include_setup=False)
        
        # Should have 3 HTML div blocks for code blocks (cells 1, 2, and 4)
        # The inline role gets cell number 3, so the last code block is cell 4
        self.assertEqual(result.count('<div id="out-'), 3)
        self.assertIn('<div id="out-1" class="cell-out"></div>', result)
        self.assertIn('<div id="out-2" class="cell-out"></div>', result)
        self.assertIn('<div id="out-4" class="cell-out"></div>', result)  # Last code block gets cell 4
        
        # Should have span for inline role (cell 3)
        self.assertIn('<span id="inline-3" class="py-inline-result">', result)
        
        # Should have graph divs for code blocks
        self.assertIn('<div id="graph-1" class="cell-graph no-mathjax"></div>', result)
        self.assertIn('<div id="graph-2" class="cell-graph no-mathjax"></div>', result)
        self.assertIn('<div id="graph-4" class="cell-graph no-mathjax"></div>', result)
        
        # Should preserve all original content
        self.assertIn("# Mixed Document", result)
        self.assertIn("Some explanation here.", result)
        self.assertIn("And inline:", result)
    
    def test_assignment_only_block(self):
        myst_content = '''# Document

```python
x = 42
y = x * 2
```
'''
        result = process_myst_document(myst_content)
        
        # Should still create HTML block
        self.assertIn('<div id="out-1" class="cell-out"></div>', result)
        self.assertIn('<div id="graph-1" class="cell-graph no-mathjax"></div>', result)
        
        # Should not have result assignment since no final expression
        self.assertNotIn("result = ", result)
    
    def test_with_setup_disabled(self):
        myst_content = '''# Document

```python
x = 42
```
'''
        result = process_myst_document(myst_content, include_setup=False)
        
        # Should not contain the setup block
        self.assertNotIn("PyScript utilities loaded successfully", result)
        self.assertNotIn("def display(obj, target=None, append=True):", result)
        
        # Should still contain the Python block and its HTML
        self.assertIn("```python", result)
        self.assertIn('<div id="out-1" class="cell-out"></div>', result)
        self.assertIn('<div id="graph-1" class="cell-graph no-mathjax"></div>', result)
    
    def test_with_setup_enabled(self):
        myst_content = '''# Document

```python
x = 42
```
'''
        result = process_myst_document(myst_content, include_setup=True)
        
        # Should contain the setup utilities in PyScript
        self.assertIn("def display(obj, target=None, append=True):", result)
        self.assertIn("def Element(element_id):", result)
        
        # Should contain the setup and execution scripts at the end
        self.assertIn("PyScript utilities loaded successfully", result)
        
        # All PyScript should be at the end
        python_block_pos = result.find("```python")
        setup_script_pos = result.find("PyScript utilities loaded successfully")
        self.assertLess(python_block_pos, setup_script_pos)

if __name__ == '__main__':
    unittest.main()
