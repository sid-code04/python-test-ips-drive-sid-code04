def longest_substring(s: str) -> int:
    """
    Implement the function longest_substring 
    using the provided length_of_longest_substring function to find 
    the length of the longest substring without repeating characters.
    """
    return length_of_longest_substring(s)

def length_of_longest_substring(s):
    # Set to keep track of characters in the current window
    char_set = set()
    
    # Left pointer for the sliding window
    left = 0
    
    # The maximum length of a substring without repeating characters
    max_length = 0
    
    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If the character at the right pointer is in the set,
        # shrink the window from the left until the character is removed
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the character at the right pointer to the set
        char_set.add(s[right])
        
        # Update the maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3 (Substring: "abc")
print(length_of_longest_substring("bbbbb"))    # Output: 1 (Substring: "b")
print(length_of_longest_substring("pwwkew"))   # Output: 3 (Substring: "wke")

import unittest

class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)
        self.assertEqual(longest_substring("bbbbb"), 1)
        self.assertEqual(longest_substring("pwwkew"), 3)
        self.assertEqual(longest_substring("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(longest_substring("aab"), 2)
        self.assertEqual(longest_substring("dvdf"), 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)