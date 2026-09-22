# Random Sentence Generator

This is a Python program that allows random generation of sentences by applying randomized phrases to a base sentence.

## How to use it

Simply save all of the included files into the same folder, then run `run.bat`.
To customize the generated sentences, make a new JSON file. Call it whatever you like, as long as it ends in `.json`. (You can also copy one of the template files.) To understand the required syntax, you can look at the template files. The object(s) with the name `SentenceTemplate` are base sentences. Mentioning a group of phrases with `[[Item$]]` (replace the $ with any number from 0 to 7) will roll a random phrase from that group and replace its mentions with the random phrase. (There is a limit of 8 phrase groups. You can modify the code if you wish to have more, but **ensure every used JSON file has those groups, even if they're not used!**)
You'll also notice a "randomcount" variable next to the first base sentence and group of randomized phrases. This is the amount of random possibilities for that section. **Make sure this always matches the amount of possibilities!** Setting the base sentence randomcount to anything below 2 will cause it to not be randomized. Setting the randomcount of a phrase group to 0 will exclude it from being randomized, and if that phrase group is mentioned in the base sentence, it won't be randomized.

## Use cases

I actually don't know what cases you'd use this in, I pretty much made it for fun