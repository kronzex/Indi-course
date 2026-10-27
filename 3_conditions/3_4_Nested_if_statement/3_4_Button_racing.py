"""
Task: Button Racing

Description:
Two people decide to compete in a typing contest on the website "Key Races." The competition requires typing a text consisting of s characters.
The first participant types one character every v1 milliseconds and has a ping of t1 milliseconds. The second participant types one character every v2 milliseconds and has a ping of t2 milliseconds.

For a participant with a ping (latency) of t milliseconds, the competition unfolds as follows:

    Exactly t milliseconds after the competition begins, the participant receives the text that needs to be typed.
    Immediately afterward, they begin typing the text.
    Exactly t milliseconds after they have finished typing the entire text, the website receives notification of this.

The winner of the competition is the participant whose notification of completion arrives first. If the notifications from both participants arrive at the same time, it is considered a tie.

Given the length of the text and the details for each participant, determine the outcome of the game.

Input:
The first line contains five integers: s, v1, v2, t1, and t2 (1 <= s, v1, v2, t1, t2 <=> 1000), representing the number of characters in the text, the typing speed of the first participant, the typing speed of the second participant, the ping of the first participant, and the ping of the second participant, respectively.

Output
If the first participant wins, output "First". If the second participant wins, output "Second". In the event of a tie, output "Friendship".

Input Example:
5 1 2 1 2

Output Example:
First
"""

s, v1, v2, t1, t2 = map(int, input().split())

time1 = s * v1 + 2 * t1
time2 = s * v2 + 2 * t2

if time1 < time2:
    print("First")
elif time1 > time2:
    print("Second")
else:
    print("Friendship")




