import unittest
from sds.sds import generate_myst_interactive

class TestGenerateMystInteractive(unittest.TestCase):
    def test_with_setup_and_final(self):
        setup = "x = 10\ny = 20"
        final = "x + y"
        cell_num = 1
        result = generate_myst_interactive(setup, final, cell_num)
        
        # Check that it contains the Python block
        self.assertIn("```python", result)
        self.assertIn("x = 10\ny = 20\nx + y", result)
        
        # Check that it contains the HTML block
        self.assertIn("```{raw} html", result)
        self.assertIn('<div id="out-1" class="cell-out"></div>', result)
        self.assertIn('<div id="stdout-1" class="cell-stdout"></div>', result)
        self.assertIn('<div id="stderr-1" class="cell-stderr"></div>', result)
        
        # Check PyScript content
        self.assertIn("<py-script>", result)
        self.assertIn("x = 10\ny = 20", result)
        self.assertIn('display(x + y, target="out-1")', result)
        self.assertIn("</py-script>", result)
    
    def test_with_only_setup(self):
        setup = "x = 42\nprint('Hello')"
        final = ""
        cell_num = 2
        result = generate_myst_interactive(setup, final, cell_num)
        
        # Check Python block
        self.assertIn("x = 42\nprint('Hello')", result)
        
        # Check HTML divs with correct IDs
        self.assertIn('<div id="out-2" class="cell-out"></div>', result)
        self.assertIn('<div id="stdout-2" class="cell-stdout"></div>', result)
        self.assertIn('<div id="stderr-2" class="cell-stderr"></div>', result)
        
        # Should not have display call
        self.assertNotIn("display(", result)
    
    def test_with_only_final(self):
        setup = ""
        final = "42 * 2"
        cell_num = 3
        result = generate_myst_interactive(setup, final, cell_num)
        
        # Check Python block contains only final
        self.assertIn("42 * 2", result)
        
        # Check HTML divs
        self.assertIn('<div id="out-3" class="cell-out"></div>', result)
        
        # Should have display call
        self.assertIn('display(42 * 2, target="out-3")', result)
    
    def test_empty_code(self):
        setup = ""
        final = ""
        cell_num = 4
        result = generate_myst_interactive(setup, final, cell_num)
        
        # Should still generate structure
        self.assertIn("```python", result)
        self.assertIn('<div id="out-4" class="cell-out"></div>', result)
        self.assertNotIn("display(", result)

if __name__ == '__main__':
    unittest.main()
