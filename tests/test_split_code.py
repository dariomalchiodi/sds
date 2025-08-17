import unittest
from sds.sds import split_code

class TestSplitCode(unittest.TestCase):
    def test_single_statement(self):
        # Assignment doesn't produce output, should go to setup
        source = 'x = 42'
        setup, final = split_code(source)
        self.assertEqual(setup, 'x = 42')
        self.assertEqual(final, '')
    
    def test_single_expression(self):
        # Expression produces output, should go to final
        source = 'x + 42'
        setup, final = split_code(source)
        self.assertEqual(setup, '')
        self.assertEqual(final, 'x + 42')
    
    def test_multiple_statements(self):
        # Last statement is assignment, doesn't produce output
        source = '''x = 1
y = 2
z = x + y'''
        setup, final = split_code(source)
        self.assertEqual(setup.strip(), 'x = 1\ny = 2\nz = x + y')
        self.assertEqual(final, '')
    
    def test_multiple_statements_with_final_expression(self):
        # Last statement is expression, produces output
        source = '''x = 1
y = 2
x + y'''
        setup, final = split_code(source)
        self.assertEqual(setup.strip(), 'x = 1\ny = 2')
        self.assertEqual(final.strip(), 'x + y')
    
    def test_empty_source(self):
        source = ''
        setup, final = split_code(source)
        self.assertEqual(setup, '')
        self.assertEqual(final, '')
    
    def test_complex_statements(self):
        source = '''def add(a, b):
    return a + b

x = [1, 2, 3]
y = list(map(lambda n: n * 2, x))

result = add(x[0], y[0])'''
        setup, final = split_code(source)
        # All statements are non-output producing, so everything goes to setup
        setup_normalized = '\n'.join(line for line in setup.split('\n') if line.strip())
        expected_setup = '''def add(a, b):
    return a + b
x = [1, 2, 3]
y = list(map(lambda n: n * 2, x))
result = add(x[0], y[0])'''
        self.assertEqual(setup_normalized, expected_setup)
        self.assertEqual(final, '')
    def test_invalid_syntax(self):
        source = 'this is not valid python'
        setup, final = split_code(source)
        self.assertEqual(setup, 'this is not valid python')
        self.assertEqual(final, '')

    def test_multiline_final_statement(self):
        # Assignment doesn't produce output, goes to setup
        source = '''x = 10
y = 20
result = (x + y) * 2 + \\
         (x - y) * 3 + \\
         x * y'''
        setup, final = split_code(source)
        setup_normalized = '\n'.join(line for line in setup.split('\n') if line.strip())
        expected_setup = '''x = 10
y = 20
result = (x + y) * 2 + (x - y) * 3 + x * y'''
        self.assertEqual(setup_normalized, expected_setup)
        self.assertEqual(final, '')

    def test_multiline_function_call_final(self):
        # Assignment doesn't produce output, goes to setup
        source = '''import math
radius = 5
area = math.pi * math.pow(
    radius, 
    2
)'''
        setup, final = split_code(source)
        setup_normalized = '\n'.join(line for line in setup.split('\n') if line.strip())
        expected_setup = '''import math
radius = 5
area = math.pi * math.pow(radius, 2)'''
        self.assertEqual(setup_normalized, expected_setup)
        self.assertEqual(final, '')

    def test_multiline_expression_final(self):
        # Expression produces output, goes to final
        source = '''import math
radius = 5
math.pi * math.pow(
    radius, 
    2
)'''
        setup, final = split_code(source)
        self.assertEqual(setup.strip(), 'import math\nradius = 5')
        expected_final = '''math.pi * math.pow(radius, 2)'''
        self.assertEqual(final.strip(), expected_final)

if __name__ == '__main__':
    unittest.main()
