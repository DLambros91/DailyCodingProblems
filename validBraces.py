import unittest


def is_valid(code):
    """

    """

    # Case the string is empty 
    if code == '':
        return True

    # Initialize the stack
    stack = []

    for i in range(0, len(code)-1):
        if i == 0 or len(stack) == 0:
            if is_closing(code[i]):
                return False
            else:
                stack.append(code[i])
        if is_closing(code[i]):
            if is_matching(stack.pop(), code[i]):
                return False
        else: 
            stack.append(code[i])
    
    if len(stack) == 0:
        return True
    else:
        return False
    
def is_closing(code):
    """
        Determine if the character is a closing brace.
        O(1)
    """

    if code == ')' or code == '}' or code == ']':
        return True
    else:
        return False

def is_matching(code1, code2):
    if code1 == '(':
        return code2 == ')'
    elif code1 == '[':
        return code2 ==']'
    else:
        return code2 =='}'

# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)