#Part 1: Discussion Questions

##Recursion

1. In your own words, what is Recursion?
	1. Something that calls itself.
2. Why is it necessary to have a Base Case?
	1. The base case is the simplest solution to a recursive task. It is the way to tell the program to stop doing that recursive task.

##Graphs

1. What is a Graph?
	1. A graph is a data structure used to show the relationship between multiple items.
2. How is a Graph different from a Tree?
	1. Trees contain branches, graphs contain loops/cycles.
3. Give an example of somthing that would be good to model with a Graph.
	1. Friends and their relationship to each other (and you) on facebook.

##Performance of Different Data Structures

Fill in the missing spots in the chart with the correct runtimes. Do this by reasoning through how the data structures work, NOT by looking up the solution. Add-R means add to the right/end/top and Add-L means add to the left/beginning. There are Xs in the spots where that operation doesn’t make sense for that data structure (for instance, you can’t index a Stack, or pop from the end of a Queue). We’ve provided the first few answers for you.

Fill in the runtimes for the following actions for the table below:

| Data Structure | Index | Search | Add-R | Add-L | Pop-L | Pop-R
| ------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| Python List (Array) | O(1) | O(n) | O(1)	  | O(n) | O(n) | O(1) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(1) | O(n) |
| Doubly-Linked List | O(n) | O(n) | O(1) | O(1) | O(1) | O(1) |
| Queue (as Array) | X | X | O(1) | X | O(n) | X |
| Queue (as LL or DLL) | X | X	| O(1) | X | O(1) | X |
| Stack (as Array, LL, or DLL) | X | X | O(1) | X | X | O(1) |
| Deque (as DLL) | X | X | O(1) | O(1) | O(1) | O(1) |
	 	 	 	 
+ **Index:** Find an item in the structure when you know its position
+ **Search:** Find an item in the structure when you know its data
+ **Add(R/L):** Set a key in set/dictionary or add node to tree
+ **Pop(R/L):** Remove a key or node

### Fill in Runtime and Memory:

The answers for Dictionary have been provided; you should fill in the rest:

| Data Structure	| Get	| Add	| Delete	| Iterate | Memory |
| ------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| Dictionary (Hash Map) |	O(1)	| O(1)	| O(1) | O(n) | medium |
| Set (Hash Map) | O(1) | O(1) | O(1) | O(n) | medium |
| Binary Search Tree | O(log(n)) | O(n) | O(n) | O(1) | low |
| Tree | O(n) | O(1) | O(1) | O(1) | low |

**Can we go over this?, Specifically for BST/Trees**

+ **Get:** Find an item in the structure
+ **Add:** Set a key in set/dictionary or add node to tree
+ **Delete:** Remove a key or node
+ **Iterate:** Find next item in data structure
+ **Memory:** Relative to data, how much memory is used? (Choices: a little, medium, or a lot)

##Sorting

1. Describe in words how the Bubble Sort algorithm works.
	1. It starts off by looking at the first two elements in an array, compares the values between the two, and swaps them to be in ascending order (if necessary). Bubble sort continues to increment by +1 until the end of the list and compares the element at the current index to the element that is one index above to see if the numbers are in order, and if not, swap. Once the first pass is done (which terminates at the end of the list), it restarts at the beginning of the list and continues this pattern until all numbers are sorted in order.
2. Describe in words how the Merge Sort algorithm works.
	1. Given two lists, A and B that are pre-sorted, compare the values at the 0th index of A and B to see which value is less. The lesser value gets popped out of list A and pushed into list C. This process continues until one of the lists are empty. The remains of the non-empty list gets appended to the end of list C.
3. Describe in words how the Quick Sort algorithm works.
	1. One difference between Quick Sort versus Merge Sort is that it heavily relies on partitions rather than combining. Quick sort takes a random value as its pivot and seeks for all items less than the pivot in order to put those lesser items to the left, and the greater items to the right. The list gets further partitioned by seeking a random value from the partition of what was previously partitioned in the last step (a pivot from each partition). Once a pivot is chosen, the values that are less than the pivots value goes to the left, and the values that are greater than the pivot's value goes to the right. The list further divides and a pivot is chosen for each partition until the list is completely sorted.

##Git Branching
1. Give an instance when you would use git branching.
	1. ~~When I don't want to have a broken project for career day and have a way to sandbox without affecting master.~~ 
	
		When I want to implement a new feature or multiple new features.
2. What is a pull request?
	1. When someone wants to merge into your branch their changes.
