

def electric_vote():
    print("*** Election ***")
    voter = {"candidate":[],"vote":[]}
    round = int(input("Enter a number of voter(s) : "))
    vote = input("").split(" ")
    if len(vote)>round:
        vote = vote[:round]
        
    for vote in vote:
         if int(vote)>0 and int(vote)<=20:
            if not vote in voter["candidate"]:
                voter["candidate"].append(vote)
                voter["vote"].append(1)
            else:
                idx = voter["candidate"].index(vote)
                voter["vote"][idx] += 1
    #print(voter)
    if(voter["candidate"]):
        #print("max ",max(voter["vote"]))
        idx = voter["vote"].index(max(voter["vote"]))
        winner = voter["candidate"][idx]
        print( winner)
    else:
        print("*** No Candidate Wins ***")
    
if __name__ == "__main__":
    electric_vote()