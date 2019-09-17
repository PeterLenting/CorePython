{"filter":false,"title":"counts.py","tooltip":"/counts.py","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":29},"action":"insert","lines":["def count_upper_case(message):","    count = 0","    for c in message:","        if c.isupper():","            count += 1","    return count","","assert count_upper_case(\"\") == 0, \"Empty string\"","assert count_upper_case(\"A\") == 1, \"One upper case\"","assert count_upper_case(\"a\") == 0, \"One lower case\"","assert count_upper_case(\"£$%%^\") == 0, \"Special characters\"","","print(\"All the tests passed\")"],"id":1}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["2"],"id":2}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"remove","lines":["2"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":5,"column":16},"action":"remove","lines":["def count_upper_case(message):","    count = 0","    for c in message:","        if c.isupper():","            count += 1","    return count"],"id":4},{"start":{"row":0,"column":0},"end":{"row":1,"column":51},"action":"insert","lines":["def count_upper_case(message):","    return sum([1 for c in message if c.isupper()])"]}],[{"start":{"row":4,"column":51},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":51},"action":"insert","lines":["assert count_upper_case(\"A\") == 1, \"One upper case\""],"id":7}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["B"],"id":8}],[{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"remove","lines":["1"],"id":9}],[{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["2"],"id":10}],[{"start":{"row":5,"column":52},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":51},"action":"insert","lines":["assert count_upper_case(\"A\") == 1, \"One upper case\""],"id":12}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["b"],"id":13},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["b"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["A"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["B"],"id":14}],[{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["1"],"id":15}],[{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["3"],"id":16}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":37},"end":{"row":6,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568715055392,"hash":"ca366e10c58b9dafcb75832d6cd040874681fbb3"}