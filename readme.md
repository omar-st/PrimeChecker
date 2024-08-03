# Prime Number Checker
======================

Table of Contents
-----------------

1. [Introduction](#introduction)
2. [How It Works](#how-it-works)
3. [Installation](#installation)
4. [Usage](#usage)

## Introduction

This is a Python program designed to check if a number less than a given maximum (default: one million) is prime.

## How It Works

The program uses the Sieve of Eratosthenes algorithm, an ancient Greek method for finding all primes smaller than a given limit. Here's how it works:

1. Initialize a dictionary of key(int) -> value(boolean) pairs.
2. Iterate through numbers from 2 to `max-1`.
3. For each number `i`, check if it is not marked as composite, and so is prime. If so, mark all multiples of `i` greater than `i` as composite by setting them to True.
4. The remaining numbers that are still marked as False in the `comp` dictionary are primes.

The program uses this algorithm to create a dictionary `primes` containing all prime numbers less than `max`.

## Installation

This code is written in Python 3.x and does not require any external libraries or dependencies. Simply copy and paste it, save it with a `.py` extension, and run it with python3.

## Usage

To use this program, simply follow these steps:

1. Run the program using `python PrimeChecker.py` 
2. The program will prompt you with a message indicating that it is checking numbers less than 10^6, and the execution time.
3. Enter a number when prompted. You can enter multiple numbers, and the program will check each one individually.
4. If the input number is prime, the program will print "{input} is prime". Otherwise, it will print "{input} is not prime".
5. Enter an empty string '' to exit.

Example use cases:

* Input: `5`
Output: `5 is prime!`
* Input: `10`
Output: `10 is not prime`

Note that this program only checks numbers less than 10^6. If you need to check larger numbers, simply modify the `max` variable in the __main__ function and re-run it.
