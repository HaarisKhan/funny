1) We define variables as so:

W: Number of words in dictionary
N: Length of string user passes in

Offline: Reading and Processing information.
Given the dictionary of size W, we split the text file into lines and read them appropriately.
Operations include creating the list, making a set of those values. These are all linear-time operations in terms of W
We can then state that the preprocessing or initialization is linear with respect to the size of the dictionary:
O(W)

Online: We find all permutations of the user string, and check if they are in the set
Use a HashMap (assuming Python3 uses HashMaps as their general dictionary).
We know that the user input word and a word in our set are anagrams of each other if their frequencies are the same.
Then all we need to do is calculate and see if their frequencies are, in fact, the same. If they are, they are anagrams of each other and we can print them out!

Exhaustive Processes: Copying list to set and such (Linear), Creating the dictionary (iterate over the user input, update map values) (Linear), Sorting (assuming QuickSort is used, Nlog(N)), and iterating over the set and calling dictMe (dictMe is a linear time with respect to N-time algorithm)
The last iteration is the most exhaustive process, with O(NW) time complexity

2) Same definitions as above

Offline:
We store the information in a dictionary in a list and eventually a set. This memory is linear in W, however many elements we desire to store from the dictionary.
O(W)

Online:
We have data structures dictionaries and set and list. A dictionary of size N worst case (all elements are distinct), a set of size W worst case, and a list of also size W worst case.
Then we have a memory constraint of whichever is larger:
O(max(N, W))

3) There is no actual need to compute all permutations of a word. For instance, with the standard dictionary of alpha, beta, etc., we know for a fact that "hello" will not return anything. None of the entries in a dictionary contain "h, e, l, o", so no possible permutation is possible.
Generally, we can think of this as follows: If the letters in the string match entirely the letters of the word in the ith iteration of the dictionary, then they are anagrams of each other
This is much faster and better than a factorial process: we can do this all in O(NW) time complexity (see above) with O(max(N, W)) space complexity
