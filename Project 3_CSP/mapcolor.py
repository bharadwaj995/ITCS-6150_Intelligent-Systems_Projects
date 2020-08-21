

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import time 


def colormap(mystatedict):
    # create the map
    plt.ion()
    map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

    # load the shapefile, use the name 'states'
    map.readshapefile('st99_d00.shp', name='states', drawbounds=True)

    state_names = []
    for shape_dict in map.states_info:
        state_names.append(shape_dict['NAME'])

    ax = plt.gca() 
    """
    seg = map.states[state_names.index('Texas')]
    seg1 = map.states[state_names.index('Washington')]
    poly = Polygon(seg, facecolor='red',edgecolor='red')
    poly1 = Polygon(seg1, facecolor='blue',edgecolor='blue')

    ax.add_patch(poly)

    for key in mystatedict:
        seg = map.states[state_names.index(key)]
        poly = Polygon(seg, facecolor=mystatedict[key],edgecolor=mystatedict[key])
        ax.add_patch(poly)
    
    
    """
    for i, seg in enumerate(map.states):
        #print("name:{}, shape:{}".format(state_names[i], seg))
        if state_names[i] in mystatedict:
            poly = Polygon(seg, facecolor=mystatedict[state_names[i]], edgecolor=mystatedict[state_names[i]])
            ax.add_patch(poly)


    plt.draw()

    plt.pause(0.0000000000001)

    """
    for i, seg in enumerate(map.states):
        #print("name:{}, shape:{}".format(state_names[i], seg))
        poly = Polygon(seg, facecolor='blue', edgecolor='blue')
        ax.add_patch(poly)
        #patches.append(poly)
        #MapAx.add_patch(poly)
   
   """
    return plt,ax





