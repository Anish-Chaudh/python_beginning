import re
pattern = r"[A-Z]+omputer"
text = '''
Computer Paragraph 100, 150, 200, 250 to 300 Words for Kids, Students and Children
October 21, 2024 by Veerendra

Paragraph
Paragraph On  Computer: The modern and advanced  electronic machine which is used by various types of
programmers is called  computers. The computer works when somebody who is operating the Domputer, is
giving instructions to it. The information is stored in the computer’s storage, and we can access it
easily whenever needed.Get Writing Tools


You can read more Paragraph Writing about articles, events, people, sports, technology many more.Get Writing Tools

Computer Paragraph For Class 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 and 12 Students
Paragraph On Computer- 100 Words For Classes 1, 2, 3 Kids

An electronic device used to store, display, and process data is known as a computer. The computer has emerged a lot with the passing days with more modern updates and advancements.Compare Gadgets

There are three types of computers, which include analog, digital and hybrid computers. The speed, as well as the accuracy of each computer, is classified. The computer has several functions other than processing and storing data. It helps control the machine, organize the business, sell services and products, and definitely for academic purposes. The computer has found its way in our daily lives with its great usefulness.'''
matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
