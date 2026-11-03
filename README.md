# Build a Wordle Solver: UC Berkeley EECS Day CS Lab

A one-hour, beginner-friendly Python lab for high school students. Students review Python basics, play Wordle, and then build their own Wordle solver step by step. At the end they compete to beat a Berkeley student's solver.

[![Open the lab in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alexmenchtchikov/EECS-Day-CS-Lab/blob/main/cs_lab.ipynb)

## Files

| File | What it is |
|---|---|
| `cs_lab.ipynb` | The student notebook. Most of the code is written, and students fill in the `___` blanks. |
| `cs_lab_solutions.ipynb` | The same notebook with every blank filled in, for TAs. |
| `wordle_setup.py` | The setup file: the 2,315-word Wordle answer bank, the playable Wordle game, exercise checkers, `test_solver`, and the competition. The notebook's first cell downloads and runs it. |

## Lab outline (~60 min)

1. **Python warm-up:** cleaning up a data file, strings, loops, `if`, lists, dictionaries
2. **Play Wordle** in the notebook
3. **Wordle's colors:** write `get_feedback` (including repeated letters)
4. **Narrow it down:** keep only the words that match the feedback so far
5. **First solver + game loop:** about 4.4 guesses on average
6. **Smarter solver:** letter frequency, about 3.7 guesses on average
7. **⭐ Bonus:** better openers, information-based guesses, and more
8. **🏆 Competition:** average guesses on 20 secret words vs. the Berkeley student

## Running the competition

Everyone who enters the same **competition code** plays the same 20 secret words. The notebook defaults to practice code `90`. For the real round, the TA announces a new code that students haven't practiced on.
