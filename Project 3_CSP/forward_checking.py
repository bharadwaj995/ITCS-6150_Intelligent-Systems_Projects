#!/usr/bin/env python

import random
from Node import Node
import pdb
from mapcolor import colormap
import time


colorlist = []

backtracks = 0

all_states = []
def init_colors(n):
    for i in range(n):
        colorlist.append(random.randint(0,255))

def random_color(n):
    return tuple(colorlist)

def build_color_graph(num,numstates,states):
    colors = random_color(3)
    a = Node(colors[0],states[0])
    root = a
    mystates = {}
    for i in range(1,numstates,1):
        w = Node(colors[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        mystates[states[i]] = a

        for j in range(1,num,1):
            b = Node(colors[j])
            a.put_child(b)
        a = w
            
    print(root)
    print(root.next)
    print(root.next[1].next)

def getcolors(states,mystatedict):
    listcol = []
    for i in states:
        listcol.append(mystatedict.get(i,""))

    return listcol

def generate_colors(states,i,numcolors,colors):
    tlist = []
    for j in range(numcolors):
        tlist.append(Node(colors[j],states[i]))

    return tlist

def forward_checking(mystatedict,statedict,numcolors,current_state,states,num):

    global backtracks
    all_states.append(mystatedict.copy())
    for i in range(len(current_state.next)):
        time.sleep(0.000002)
        mystatedict[current_state.next[0].myname] = current_state.next[i].mycolor   
        if mystatedict.get(current_state.next[0].myname) in getcolors(statedict[current_state.next[0].myname],mystatedict):
            #print("continued")
            continue  
        if num == len(states) - 1:
            return 1,mystatedict

        temp_colorlist = colorlist.copy()
        remove_colors = getcolors(states[num+1],mystatedict)
        temp_colorlist = [x for x in temp_colorlist if x not in remove_colors]
        current_state.next[i].next = generate_colors(states,num+1,numcolors,temp_colorlist)

        ans = forward_checking(mystatedict,statedict,numcolors,current_state.next[i],states,num+1)
        if ans[0] == 1:
            return 1,mystatedict

        continue
        
    backtracks +=1

    return 0,mystatedict 


def init(states,statedict,numcolors):
    colors = colorlist
    root = Node(colors[0],states[0])
    for j in range(numcolors):
        root.put_child(Node(colors[j],states[0]))

    return root
    



        


            
            
    
    
if __name__ == "__main__":
    numcolors = 4
    init_colors(numcolors)

    colorlist = ["red","blue","green","black"]

    statedict = {
'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
'California':['Arizona', 'Nevada', 'Oregon'],
'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
'Florida':['Alabama', 'Georgia'],
'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
'Maine':["New Hampshire"],
"Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
'Mississippi':['Alabama', 'Arkanssas', 'Louisiana', 'Tennessee'],
'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
'New Jersey':["Delaware", "New York", "Pennsylvania"],
'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
'South Carolina':['Georgia', 'North Carolina'],
'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
'Washington':['Idaho', 'Oregon'],
'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
"Hawai":[],
"Alaska":[]
}


    #states = ['Illinois', 'Oklahoma', 'California', 'Utah', 'Wyoming', 'Missouri', 'Michigan', 'Texas', 'Iowa', 'Delaware', 'Tennessee', 'Maryland', 'Kentucky', 'Montana', 'Minnesota', 'Connecticut', 'Louisiana', 'West Virginia', 'Pennsylvania', 'Nebraska', 'Kansas', 'Indiana', 'Rhode Island', 'Arizona', 'Florida', 'Massachusetts', 'South Dakota', 'Nevada', 'South Carolina', 'Ohio', 'New Hampshire', 'Idaho', 'Washington', 'Colorado', 'Oregon', 'New Jersey', 'Mississippi', 'Arkansas', 'Vermont', 'Wisconsin', 'Alabama', 'Georgia', 'Maine', 'New Mexico', 'North Carolina', 'New York', 'Virginia', 'North Dakota']

    states = ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'Colorado', 'Mississippi', 'Arkansas']

    """
    states = ['Kansas', 'New Hampshire', 'Idaho', 'Louisiana', 'New Jersey', 'Arkansas', 'Kentucky', 'Maine', 'Minnesota', 'Missouri',
            'West Virginia', 'North Carolina', 'Massachusetts', 'Michigan', 'Indiana', 'Illinois', 'Virginia', 'Oklahoma', 'Montana',
            'North Dakota', 'Texas', 'Colorado', 'South Carolina', 'Maryland', 'California', 'New York', 'Florida', 'Vermont', 'Utah',
            'Georgia', 'Oregon', 'Wisconsin', 'Rhode Island', 'Nebraska', 'New Mexico', 'Mississippi', 'Alabama', 'Nevada', 'Tennessee',
            'Iowa','South Dakota', 'Ohio', 'Pennsylvania', 'Washington', 'Wyoming', 'Arizona', 'Delaware', 'Connecticut']


    
    states=['wa','nt','q','nsw','v','sa']

    statedict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
    
    
    """

  
    mystatedict = {}
    
    print(states)

    #print(states)
    root = init(states,statedict,numcolors)

    start_time = time.time()
    answer = forward_checking(mystatedict,statedict,numcolors,root,states,0)
    end_time = time.time()
    count = 0 
    for key in answer[1]:
        count+=1
        if answer[1][key] in getcolors(statedict[key],mystatedict):
            print("oops")


    print("VERIFIED ANSWER")
    print(answer)
    print("NUMBER OF BACKTRACKS: "+ str(backtracks))
    print("TIME OF EXECUTION: " + str(end_time - start_time) + "seconds") 

    print(len(all_states))

    for i in range(0,len(all_states),2000):
        colormap(all_states[i])


    colormap(mystatedict)

    time.sleep(10)
    


