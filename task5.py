def string_length(word):
  count = 0
  for length in word:
    count += 1
    
  return count

#DO NOT remove lines below here, this is designed to test your code.
def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below

test_string_length()