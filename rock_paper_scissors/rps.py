#!/usr/bin/python

import sys

plays = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
  outcomes = []

  def possible_outcomes(roundsLeft, result):
    if roundsLeft == 0:
      outcomes.append(result)
      return
    for play in plays:
      possible_outcomes(roundsLeft - 1, result + [play])

  possible_outcomes(n, [])
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')