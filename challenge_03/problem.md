Challenge 3 - Lost in Lost
========

The writers of the Lost series have a serious problem. Due to its immense
popularity, they have written several hundred seasons. Almost every chapter
has some flashbacks or flashforwards that display scenes of other chapters of
other seasons, that may have been written, or may not have.

In order to write a book of the complete series, they want to have all scenes
arranged chronologically, but they are lost in their scripts (what a shame!).
They have hired you to solve this.

Input:

* First a number N of scripts to process is given. Then, N scripts follow,
each one in a different line.

* Each script consists of a sequence of described scenes. Each scene is
delimited by a dot (.), a less-than ( < ) or a greater-than ( > ) symbol:

    Scenes beginning with the dot are chronologically ordered.
    If the scene begins with a < symbol, then it's a flashback during the previous (chronologically ordered) scene. That is, it happened before the previous scene.
    If the scene begin with a > sign, then it's a flashforward during the previous (chronologically ordered) scene. That is, it happened after the previous scene.

* Example: .A>B<C is C,A,B

There may not be any possible chronological order for a given script, or there
may be more than one if the scriptwriters have made enough of a mess.

Output:

For each script, if there is only one possible chronological order, output the
list of scenes described, ordered chronologically and separated by commas.

If the script has a finite number (greater than 1) of possible chronological
orders, return 'valid'.

If no chronological order is possible, or there is more than one beginning or
end scene, or there is neither beginning nor end scene, then return 'invalid'.

Sample input:

    3
    .john gets into the plane<john sees paul at the airport.john tells mia they are going to die>the plane crashes
    .john gets into the plane<john sees paul at the airport.john tells mia they are going to die>the plane crashes.the plane takes off.mia sees through the window an isolated island<the plane crashes
    .john gets into the plane<john sees paul at the airport.john tells mia they are going to die>the plane crashes.john sees paul at the airport

Sample output:

    john sees paul at the airport,john gets into the plane,john tells mia they are going to die,the plane crashes
    valid
    invalid
