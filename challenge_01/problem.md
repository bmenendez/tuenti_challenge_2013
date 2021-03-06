Challenge 1 - Bitcoin to the future
===========

In the near future, after winning the Tuenti Challenge, you acquire almost
supernatural programming skills. You write a Flux Capacitor Algorithm that is
able to predict the exchange rate in euros of Bitcoin (the most used Internet
currency) for a period of time. Now, you need to write a program that, given a
list of Bitcoin exchange rates for a period of time and your initial budget,
calculates the maximum number of euros that you are going to have at the end
of the period. That is, the amount of euros you can earn plus your initial
budget.

The exchange rate is always an integer, you can't buy a fraction of a bitcoin
and you can sell or buy bitcoins at any moment, as many times as you want.

Input:

    First line contains the number of test cases, T, and T cases follow (each one in a different line).
    Each test case consists of one integer N (1 ≤ N ≤ 100), indicating your initial budget in euros.
    In the next line, there is a list of integers indicating the future value of Bitcoin at different times in a fixed period.

Output:

    The maximum amount of euros that you will have at the end, in a different line for each test case.

Example:

* Initial budget: 3
* List of exchange rates: 1, 2, 10, 6

You buy at 1 euro per bitcoin and sell at 10 euros per bitcoin, so at the end
you will have 30 euros.

Sample input:

    2
    2
    1 2 10 4 1 10
    5
    1 2 4 20 5 30 4 25 7

Sample output:

    200
    3750
