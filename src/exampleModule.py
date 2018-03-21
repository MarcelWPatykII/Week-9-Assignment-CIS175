'''
Created on Mar 21, 2018

@author: mpaty
'''
import sys;

def addNumbers():
    number = 0;
    arrayOfNumbers = [];
    
    while(number != -1):
        number = int(input("Please enter a number. Enter -1 to stop."))
        arrayOfNumbers.append(number);
        
    return arrayOfNumbers;

def orderNumbersAscending(array):
        for i in range(0, len(array) - 1):
            for j in range(0, len(array) - 1):
                if(array[j] > array[i]):
                    tempValue = array[i];
                    array[i] = array[j];
                    array[j] = tempValue;
               
        return array;           

def orderNumbersDescending(array):
        for i in range(0, len(array) - 1):
            for j in range(0, len(array) - 1):
                if(array[j] < array[i]):
                    tempValue = array[i];
                    array[i] = array[j];
                    array[j] = tempValue;
                    
        return array;

def createMenu():
    print("\t----------------------------------\n\t|Welcome to the Number Organizer!|\n\t----------------------------------\n 1.) Organize by Ascending\n 2.) Organize by Descending\n 3.) Quit");
    
    userChoice = input();
    
    if(userChoice == "1"):
        print("\n"*50);
        
        unsortedArray = addNumbers();
        ascendingArray = orderNumbersAscending(unsortedArray);
        for i in range(0, len(ascendingArray) - 1):
            print(ascendingArray[i]);
            
        print("Type 'menu' to return to the menu.");
        userChoice = input();
        
        if(userChoice == "menu"):
            print("\n"*50);
            createMenu();

    if (userChoice == "2"):
        print("\n"*50);
        
        unsortedArray = addNumbers();
        descendingArray = orderNumbersDescending(unsortedArray);
        for i in range(0, len(descendingArray) - 1):
            print(descendingArray[i]);

        print("Type 'menu' to return to the menu.");
        userChoice = input();
        
        if(userChoice == "menu"):
            print("\n"*50);
            createMenu();
    
    if (userChoice == "3"):
        sys.exit();
createMenu();

'''                                  
unsortedArray = addNumbers();

for i in range(0, len(unsortedArray) -1):
    print(unsortedArray[i]);
  
ascendingArray = orderNumbersAscending(unsortedArray);

for i in range(0, len(ascendingArray) - 1):
    print(ascendingArray[i]);
'''