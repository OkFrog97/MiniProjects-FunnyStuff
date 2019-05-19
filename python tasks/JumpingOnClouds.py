def jumpingOnClouds(c):
    '''
    Return minimal player's jumping on clouds.
    C - is list of clouds where 0 is good cloud and 1 - danger cloud.
    Player can jump on first or second cloud before him.
    Example:
    >jumpingOnClouds([0,0,0,1,0,1,0,0])
    >4
    >
    >jumpingOnClouds([0,1,0,0,1,0])
    >3
    '''
    
    #add vars
    player = 0 #player position on clouds
    jumps = 0
    last_cloud = len(c)-1
    
   
    #find minimal jumps
    while player != last_cloud:
        if  player+2 <= last_cloud and c[player+2] == 0:
            player += 2
        else:
            player += 1
        jumps += 1  
            
    #return result
    return jumps

def main():
    print (jumpingOnClouds([0,0,0,1,0,1,0,0]))
    print ('Answer: 4')
    print (jumpingOnClouds([0,1,0,0,1,0]))
    print ('Answer: 3')
    print (jumpingOnClouds([0,0,1,0,0,1,0]))
    print ('Answer: 4')
    print (jumpingOnClouds([0,0,0,1,0,0]))
    print ('Answer: 3')
    
if __name__ == "__main__":
    main()