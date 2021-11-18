# Off-line elevators allocation system
> made by Elad Seznayev and Nerya Bigon.
* As part of OOP course assignment.

Our goal in this repository is to creat an off-line elevator allocation algorithm, that works as efficiently as possible.
we define efficiency as reducing the time passed from the moment a call was received until the elevator reached the destination.

## Approach:
An offline elevators allocation algorithm is an algorithm, design to allocate elevators to passengers when all the input is given in advance.  
The fact that the input is already known, on one hand give the algorithm extra time to calculate the best allocation posible.  
But on the other hand introduce a complication to the problem of allocation - the need to simulate somehow the movment of the elevators, in order to calculate the location of each elevator in any given moment.  

For more information on this topic we recommend reading the following articles:
* This one dive deep into the subject, it helped us specipicly on it's unique approach to offline algorithm (page 70) - https://1drv.ms/b/s!AuDWVVpV6-rC7na9FC_0fi-pJ1Ig?e=vevmW4  
* This one gave us (on page 146) a point to think about with regard to online algorithm - tha algorithm has to work within a certain time limit -  https://repository.lboro.ac.uk/articles/thesis/An_intelligent_real-time_lift_scheduling_system/9539087/files/17168627.pdf  

* In this one we were introduced to the idea of dynamic partition of elevator allocation system - http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.8791&rep=rep1&type=pdf  



## Offline Algorithm:
Because we do not simulate the elevators movment, most of the work our algorithm do involve mostly the information that is already in the calls file.
Essentially for every elevator the algorithm attemt to create the longest list posible of a calls that will overlap with each other in term of times, floor range and direction of travel.  
Once every elevator got their first list, the calls on that list are allocated to the output and the algorithm perform the same steps repeatedly until it get "stuck" - meanning, it can no longer perform without exceeding a list boundaries.  


#### the algorithm in steps: 
1. Loop on every elevator in the building, and for every elevator loop on every call in the call list, and for every call loop again on all the rest of the calls.
2. Check if the current call is in the time frame of the main call we are on. If so, check if it is in the same direction and that the source floor of the current call is between the source and destination of the main call. 
3. If it is, append it to a list of the main call.
4. Append the list to a list of the current elevator.
5. Find the longest list in the elevator list of calls lists and allocate those calls to the current elevator.
6. After doing so for all of the elevators, do so again until you can't.
7. Allocate remainimg calls if there are any.

## Project Structure:
Class | description
----- | -----------
`Ex1` | the main function that run the program.
`Algo` | the algorithm itself, calculate the best elevator for a call and allocate it.
`Building` | building class, that initialize a building from a json file. 
`Call` | call class that initialize a calls list from a csv file, and write the final allocation to a csv output file.
`Elevator` | Elevator class, creat an elevator from a list.

## Results:
* results from the simulator provided.  

Building | Calls Case | Avrage waiting time 
-------- | ---------- | ------------------- 
B1 | a | 112 
B2 | a | 47 
B3 | a | 31 
B4 | a | 21 
B5 | a | 18    

Building | Calls Case | Avrage waiting time 
-------- | ---------- | ------------------- 
B3 | b | 589 
B4 | b | 251 
B5 | b | 73  

Building | Calls Case | Avrage waiting time 
-------- | ---------- | ------------------- 
B3 | c | 579 | d |553 
B4 | c | 253 | d |257 
B5 | c | 73 | d | 70    

Building | Calls Case | Avrage waiting time 
-------- | ---------- | ------------------- 
B3 | d |553 
B4 | d |257 
B5 | d | 70

## How to run:
#### run the algorithm: 
------------------------
make sure the necessary files are in the same folder, the files are:
1. The project folder (Ex1).
2. A JSON building file on the same level of the Ex1.py file (inside the src folder).
3. A CSV calls file on the same level of the Ex1.py file (inside the src folder).

Next, open a terminal window in the src folder and run the following command:  

```
python3 Ex1.py <building.json> <calls.csv> <output.csv>
```  
The output file can be found in the out folder.

#### run the test simulator:
-----------------------------
make sure the necessary files are in the same folder on the first level, the files are:
1. The jar simulation file.
2. A JSON building file.
3. A CSV calls file that was generated using the algorithm.

Next, open a terminal window in this folder and run the following command:  
```
java -jar Ex1_checker_V1.2_obf.jar <ID,ID> <building.json> <calls.csv> <output.log>
```
