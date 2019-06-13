#!/usr/bin/env python
import sys

def Last_To_First_Name(Name):
	TempArrName = Name.split(" ")
	TempArrName.insert(0, TempArrName.pop())
	return " ".join(TempArrName)


def First_To_Last_Name(Name):
	TempArrName = Name.split(" ")
	TempArrName.append(TempArrName.pop(0))
	return " ".join(TempArrName)


def Sort_Name(NameList):
	for idx in range(len(NameList)):
		NameList[idx] = NameList[idx].lower()
		NameList[idx] = Last_To_First_Name(NameList[idx])

	NameList.sort()
	
	for idx in range(len(NameList)):
		NameList[idx] = First_To_Last_Name(NameList[idx])
		NameList[idx] = Captalize_First_Letter_In_Name(NameList[idx])

	return NameList

def Captalize_First_Letter_In_Name(Name):
	TempArrName = Name.split(" ")
	for idx in range(len(TempArrName)):
		TempArrName[idx] = TempArrName[idx].capitalize()
	return " ".join(TempArrName)


#Main
def main():
	FilePath = "./unsorted-names-list.txt"
	if len(sys.argv) == 2:
	    FilePath = sys.argv[1]

	with open(FilePath, "r") as UnsortedNameFile:
		NameList = UnsortedNameFile.read().splitlines()

	NameList = Sort_Name(NameList)

	for idx in range(len(NameList)):
		print(NameList[idx])

	with open("sorted-names-list.txt", "w") as SortedNameFile:
	    for Name in NameList:
	        SortedNameFile.write("%s\n" % Name)


if __name__ == "__main__":
	main()