import random, string, time, math, os, sys

keysdone = 0
totalkey = math.pow(62, 8)
fixedkey = format(totalkey, '.0f')
key = "5c4GDxv4"
result = ""
keysasec = 0
passlist = "pass.txt"
fp = open(passlist, 'wb')
start = time.time()
while key != result:
        try:
                char_set = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.digits
                #char_set = string.digits + string.ascii_lowercase
                result = ''.join(random.sample(char_set*6, 8))
                end = time.time()
                curtime = end - start
                fixedtime = format(curtime, '.0f')
                keysleft = int(fixedkey) - int(keysdone)
                print "Key: %s Generation: %s Time Elapsed: %s Possible Keys: %s" % (result, keysdone, fixedtime, keysleft)
                if result == key or keysleft == 0:
                        print "%s = %s" % (result, key)
                        print "Keys generated: %s" % keysdone
                        exit()
                else:
                        fp.write(result + "\n")
                        keysdone += 1
        except (KeyboardInterrupt, SystemExit):
                print "\n"
                print "Current key: %s Keys generated: %s Total time ran: %s" % (result, keysdone, fixedtime)
                fp.close()
                exit()
