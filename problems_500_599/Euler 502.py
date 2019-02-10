"""
Thoughts:
The number of blocks in any given row is given by:

            Draw a horizontal line through the row
            Count the number of vertical lines you pass through
            Halve it

The sum of all blocks must be even.
This means that the total number of verticals you pass through must be divisible by four.

Moreover, the number of blocks can be given by counting the steps upwards and downwards then dividing by two.

Consider the (6, 4) castle below.

  0
0 0 0
000 00
000000

up, up, up, across, down, across, up, up, across, down, down, down, across, up, up, across, down, across, down, down

This is seven up, seven down. (7 + 7) / 2 = 7. There are therefore seven blocks.

Demanding that there are an even number of blocks gives: 4x = u + d, where x is an integer and u, d are steps up, down.


Now, the maximum number of steps depends on the evenness of the width.
for even w: max steps = 2h + (w - 2)(h - 1)
 for odd w: max steps = 2h + (w - 1)(h - 1)

The minimum number of steps varies for odd or even h.
for even h: min steps = 2h
 for odd h: min steps = 2(h + 1)



Ignore odd cases? Not relevant to question

"""

# Ended up writing in sage
