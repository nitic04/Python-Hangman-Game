# Python Hangman Game

## Table of Contents
* [Languages Used](#languages-used)
* [Setup](#setup)
* [Features](#features)
* [Updates](#updates)

## Languages Used
- Python

## Setup
1. Download the python file (main.py)
2. Open the file in an IDE (VSCode, Replit, etc)

## Features
- randomly selects a word from a list
- prints spaces to represent each letter in the word
- options where user can either guess a letter or guess the word
- part of hangman is added each time an incorrect letter is guessed
- when a correct letter is guessed the empty space where that letter goes is filled in everytime it appears
- if user incorrectly guesses 6 times, the game ends with a message and quits
- if the user correctly guesses the word, the game ends with a winning message and quits

## Updates
- July 21st: started the project
- August 4th update: added ability to replay the game 
- August 8th update: added some exception handling for integer inputs, allowed for game to proceed with incorrect guesses, allowed randomization of themes and words using txt files, prohibited the same letter from being guessed multiple times
- August 9th update: added three modes of word difficulties for both themes
