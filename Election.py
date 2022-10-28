print("*** Election ***")
voter = {"candidate":[],"vote":[]}
voter = int(input("Enter a number of voter(s) : "))
if int(voter) <= 20:
  for i in range(voter):
      vote = input()
      if int(vote)>0 and int(vote)<20:
            if not vote in voter["candidate"]:
                voter["candidate"].append(vote)
                voter["vote"].append(1)
            else:
                idx = voter["candidate"].index(vote)
                voter["vote"][idx] += 1




 #vote = input()
   # votelist.append(vote)
#else:
    #print("error")    
#print(votelist)
#print()