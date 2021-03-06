Challenge 4 - Missing numbers
===========

Here at Tuenti we use integer numbers a lot. We store all of them (only
non-negative integers, from 0 to 231-1) in a binary file inside a USB drive.
Yesterday, while playing rollerball, we accidentally dropped it. Integers were
shuffled around and we have lost 100 of them. We are really devastated. Help
us find the missing ones!

[Here](https://mega.co.nz/#!r8JHzCIS!Y9mjQD2QC57Vuvvtv9o0yRIqk3p1ZI7l2LsQVrlb9n4) you have a (7z) file with the current content of the USB drive, and just
to be sure you are reading it correctly, the first number in the file is
2147459344.

Input:

The first line contains the number of test cases, T, and T cases follow (each
one in a different line). Each test case consists of one integer N (1 ≤ N ≤
100), indicating that you must find the Nth missing integer in the file (in
ascending order).

Output:

The Nth missing number in the file, in a different line for each test case.

Example:

Suppose that all numbers from 0 to 107 are in the file, and that 108 is the
first integer missing in the file. Then, if you are asked to provide the 1st
missing number, you will have to ouput 108.

Sample input:

    2
    3
    98

Sample output:

    9854
    2147478824
