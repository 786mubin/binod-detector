with open("binod.txt","r") as f:
    for line in f:
        word=line.lower().split()

        for binod in word:
            if(binod=="binod"):
                print("Founded")
            else:
                continue
                
