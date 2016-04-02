import matplotlib.pyplot as plt

#formulae - Newtons law of Gravitation

#f - force of gravity
#g - gravitational constant = 6.674 * (10**-11)
#m1 - mass of object 1
#m2 - mass of object 2
#r2 - distance btween object 1 n 2

def main():
    gen_graph()


#using matplotlib.pylot to draw graphs

def create_graph(x, y):
    
    
    plt.plot(x, y, marker='o')
    
    plt.title("Newton gravitational Force and Distance")
    
    #plt.legend([x, y])
    
    plt.ylabel("Gravitational force in newtons")
    
    #plt.axis(ymin=0)
    
    #plt.axis(ymax=20)
    
    plt.xlabel("Distance in meters")
    
    #plt.axis(xmin=0)
    
    #plt.axis(xmax=20)
    
    plt.show()


def gen_graph():
    #generate value for r
    r = range(100, 1001, 50)
    
    #generate list of f
    f=[]
    
    #constant g
    g = 6.674 * (10**-11)
    #two masses
    m1 = 0.5
    m2 = 1.5
    
    #calculate force and append it in f
    for d in r:
        force = g*(m1*m2) / (d**2)
        f.append(force)
    
    #call the create graph function
    create_graph(r, f)
    
    
    
if __name__ == "__main__":
    main()
