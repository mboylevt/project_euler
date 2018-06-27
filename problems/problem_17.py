one = two = six = ten = 3
four = five = nine = 4
three = eight = seven = forty = fifty = sixty = 5
eleven = twelve = twenty = thirty = eighty = ninety = 6
hundred = fifteen = sixteen = ninteen = seventy = 7
thirteen = fourteen = eighteen = nineteen = 8
seventeen = 9

sum = \
    (ten * 10) + (hundred * 99 * 9) + ((eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen) * 10) + \
    ((twenty+thirty+forty+fifty+sixty+seventy+eighty+ninety) * 10 * 10) + ((one+two+three+four+five+six+seven+eight+nine) * 4 * 9) + 7 + 3*899

print(str(sum))

# this is dumb