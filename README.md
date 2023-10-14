# CS50_Final_Project
[Video] (https://youtu.be/0ph8xrIDUGI)
## Description
The Single Elimination Tournament Simulator allows user to spend their time and have fun with the real tournament.

## Requirement
There are no requirment for compling this program

## How To Use
### Step 1: Number of Teams
Enter a correct number to choose the number of team joining the tournament.

<img width="314" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/6d6d4b8a-5ef8-47bb-981a-eebd9f53c1c5">

### Step 2: Name of Teams
Enter all the team name. Repeated name will be rejected.

<img width="200" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/57df3beb-8235-4df3-b655-a126dce7e68d">


### Step 3: Rating for Teams
Enter the rating for each team to simulate the win rate. Out of range or non-numeric input will be rejected.

<img width="261" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/2e27652e-3105-4c16-9981-1e0376322009">

### Step 4: Confirmation
Check if you want to adjust the data.

<img width="230" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/8d102794-002d-4cc1-b01a-40a4a621d081">

### Step 4.1: Adjusting teams
Enter the name of team you want to adjust. A name have not been entered before will be rejected.
You can choose to adjust the name, rating or both. Repeated name, out of range or non-numeric input will be rejected.

<img width="256" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/1e296aa5-a52f-457a-b924-394e08852d99">
<img width="234" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/a94e4461-d536-4d9d-a869-7fbc0cac4e73">

### Step 5: Matching Stage
Choose which types of matching, randomly or selecting by yourself.

Choosing randomly:

<img width="243" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/7d5f851d-3cd6-4280-88c3-45ff893fc12d">

Selecting by yourself:

<img width="197" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/d0a000fb-667f-442a-9116-33668199015d">

### Step 6: Generating the result
For each matching, the program will choose a random number from sum of the rating of both team.

For example, JDG: 10 and BLG: 7, the range for randint will be 17. If it chooses a number smaller or equal to 10, the winner will be JDG. Otherwise, BLG will be the winner.
The result will be generated within a few second.

<img width="290" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/d3ad9435-c0f7-41a6-958c-91a738a65aa2">

### Step 7: Outputting as file
Enter "YES" to output the result as file "Random_Champion_Result.txt"
Enter any other thing to not output

<img width="291" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/daf8e823-185a-43df-b115-0491d6980ad0">

### Step 8: Play Again or Not
Enter a number to simulate a new tournament with new set of data or teriminate the program

<img width="291" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/1a491179-7130-40c7-9534-dc06ac7b563a">

### Example File

<img width="382" alt="image" src="https://github.com/Chow309/CS50_Final_Project/assets/94815705/1d30c23c-25cd-45ae-9ce3-b489080bfaf0">





