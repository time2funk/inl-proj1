About
_____
The python script was written by s15928


Instruction
___________
1) Open python
2) Start project.py
3) Folow the instructions on the screen
3.1) Enter the name of text file.. (for ex "MyText") 
3.2) It should be in the same directory as project.py
4) Enjoy!


What its do?
____________
-It takes some "file_name.txt"
-Read it
-Parse text in it 
-And in the end give the result.xml with parsed text in to paragraphs and sentences.


How it works?
_____________
The script use Python Regular Expressions to parse the text and to fine the ends of paragraphs or sentences in different cases.
['\n' , '.!?']
It uses few patterns for Regular Expressions to find some exeptions in text. 
For example: ['ex.' ,  'prof.' ,  'A.' , '20.']
This abbreviations ends with point in the end but its not the end of the sentence!
