# Practical Documentation Of Name Sorter
This program is tested using Ubuntu 17.10 with Python installed

## Preparation:
Make sure "name-sorter.py" and your unsorted name txt file in the same directory

## How to run the program:
1. Open Terminal on the same directory as the program (name_sorter.py)
2. Run "cp name_sorter.py /usr/local/bin"
3. Run "name_sorter.py ./(FILENAME)" (If you do not enter "./(FILENAME)", then it will use "unsorted-names-list.txt" as FILENAME)

## How to run unit tests:
1. Open Terminal on the same directory as the program (unit_test.py)
2. Run "python unit_test.py"

## The Contents Of The Unit Tests:
1. Test Last_To_First_Name function if all names has 1 given name 
2. Test Last_To_First_Name function if all names has 2 given names 
3. Test Last_To_First_Name function if all names has 3 given names
4. Test First_To_Last_Name function if all names has 1 given name 
5. Test First_To_Last_Name function if all names has 2 given names 
6. Test First_To_Last_Name function if all names has 3 given names
7. Test Short_Name function
8. Test Sort_Name function if there is(are) a random shorted name(s)
9. Test Short_Name function if all names are in lowercase
10. Test Short_Name function if all names are in uppercase
11. Test Short_Name function if all names are in random lower-uppercase
12. Test Short_Name function if all last names are same
13. Test Short_Name function if all shorted last names are same
14. Test Short_Name function if all names has 1 given name
15. Test Short_Name function if all names has 1 shorted given name
16. Test Short_Name function if all names has 2 given name
17. Test Short_Name function if all names has 2 shorted given name
18. Test Short_Name function if all names has 3 given name
19. Test Short_Name function if all names has 3 shorted given name
20. Test Captalize_First_Letter_In_Name function if all names are in lowercase
21. Test Captalize_First_Letter_In_Name function if all names are in uppercase
22. Test Captalize_First_Letter_In_Name function if all names are in random lower-uppercase