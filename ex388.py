﻿# ---  coding：UTF-8  ten_things="apple orange crow telephone light suger"print "no 10 things in the list ,let's fix it "stuff=ten_things.split(' ')more_stuff=["day","night","song","fri","corn","bana","girl"]while len(stuff)!=10:    next_one=more_stuff.pop()    print "adding  ",next_one    stuff.append(next_one)    print "there is %d items now"%len(stuff)print "there we go :" ,stuffprint "let 's do some things with stuff"print stuff[1]print stuff[-1]    #the last oneprint stuff.pop()print ' '.join(stuff)                      # 使用' '来合并print '#'.join(stuff[3:5])                  # 使用# 来合并