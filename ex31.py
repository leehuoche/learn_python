

print "you enter a room ,and you choose two doors 1 or 2"

door=raw_input("<")

if door=="1":
    print "the bear is eating a cake.what do u do "
    print "1. take a cake"
    print "2. scream at the bear"

    bear=raw_input("<")

    if bear=="1":
        print "bear eat you face"
    elif bear=="2":
        print "bear eat you leg"
    else:
        print "do %r id a good jog" %bear

elif door=="2":
    print "you retina"
    print "1. blue"
    print "2. yellow"
    print "3. melodies"

    insanity=raw_input(">")

    if insanity=="1"or insanity=="2":
        print "you survives by jello"
    else:
        print "the insantity rots your eyes"

else:
    print "you stumble around and fall on a knife die"