import unittest
from sds.sds import generate_pyscript_setup

class TestGeneratePyscriptSetup(unittest.TestCase):
    def test_generate_setup(self):
        result = generate_pyscript_setup()
        
        # Should be a raw HTML block
        self.assertIn("```{raw} html", result)
        self.assertIn("<py-script>", result)
        self.assertIn("</py-script>", result)
        
        # Should define the display function
        self.assertIn("def display(obj, target=None, append=True):", result)
        
        # Should define the Element helper class
        self.assertIn("def Element(element_id):", result)
        self.assertIn("class ElementWriter:", result)
        
        # Should have write, append, and clear methods
        self.assertIn("def write(self, content):", result)
        self.assertIn("def append(self, content):", result)
        self.assertIn("def clear(self):", result)
        
        # Should make functions globally available (PyScript/Pyodide compatible)
        self.assertIn("import builtins", result)
        self.assertIn("builtins.display = display", result)
        self.assertIn("builtins.Element = Element", result)
        
        # Should log success message
        self.assertIn("PyScript utilities loaded successfully", result)

if __name__ == '__main__':
    unittest.main()
