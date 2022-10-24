from PIL import Image
from copy import deepcopy
m,n = 1000,1000
new = Image.new('RGB',(m,n),(255,255,255))
cc=[(255,255,255),(200,0,0),(0,200,100),(0,0,200)]
def f(x,c):#coefficient of the polynomial
    return x**3-c
def df(x):#first derivative of the function
    return 3*x**2
def newton(init,c):
    cur = init
    times = 0
    while times<=100:
        d = f(cur,c)/df(cur)
        if abs(d)<0.00001:#converge to a root
            return cur
        times+=1
        cur-=d
    return False#diverge
def classify_root(z):
    if abs(z.imag)<0.00001:#real root
        return 1
    if z.imag<0:#root with negative imaginary part
        return 2
    if z.imag>0:#root with positive imaginary part
        return 3
    return 0
frames=[]
for c in range(20):
    for i in range(m):
        for j in range(n):
            ii = 10*i/(m-1)-5
            jj = 10*j/(m-1)-5
            z = complex(ii,jj)
            zz = newton(z,10*c)
            if zz != False:   
                new.putpixel((i,j),cc[classify_root(zz)])#coloring by the root it converges to
            else:
                new.putpixel((i,j),(255,255,255))      
    frames.append(deepcopy(new)) 
frames[0].save('newton_fractal.gif',save_all=True,append_images=frames[1:],optimize=False,duration=100,loop=0)