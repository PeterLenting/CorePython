{"filter":false,"title":"evens.py","tooltip":"/evens.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":51,"column":26},"action":"insert","lines":["\"\"\"","Solution to the challenge in the `Test Before` unit found in the `Test Driven","Development with Python lesson`","NOTE: The solution found in this file is one of the many potential solutions","that can be used to achieve the end result expected by the challenge in the","lesson.","\"\"\"","","","def even_number_of_evens(numbers):","    \"\"\"","    Returns the number of even numbers contained in a list of numbers.","    `numbers` should be a list containing numbers","    ","    Returns either True or False based on a number of criteria.","        - if `numbers` is empty, return `False`","        - if the number of even numbers is odd, return `False`","        - if the number of even numbers is 0, return `False`","        - if the number of even numbers is even, return `True`","    \"\"\"","","    # Check to see if the list is empty","    if numbers == []:","        return False","    else:","        # Set a `number_of_evens` variable that will be incremented each time","        # an even number is found","        evens = 0","        ","    # Iterate of over each item and if it's an even number, increment the","    # `evens` variable","    for number in numbers:","        if number % 2 == 0:","            evens += 1","    ","    if evens == 0:","        return False","    else:","        return evens % 2 == 0","","# Our set of test cases","assert even_number_of_evens([]) == False, \"No numbers\"","assert even_number_of_evens([2]) == False, \"One even number\"","assert even_number_of_evens([2, 4]) == True, \"Two even numbers\"","assert even_number_of_evens([2, 3]) == False, \"Two numbers, only one even\"","assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, \"Multiple numbers, three even\"","assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, \"Multiple numbers, four even\"","assert even_number_of_evens([1, 3, 9]) == False, \"No even numbers\"","","# If all the test cases pass, print some successful info to the console to let","# the developer know","print(\"All tests passed!\")"],"id":1}]]},"ace":{"folds":[],"scrolltop":362.3125,"scrollleft":0,"selection":{"start":{"row":51,"column":26},"end":{"row":51,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1568717968330,"hash":"c7e4c7ae5f274417d3807fb3a0cdbddcb363cfe1"}