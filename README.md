# operator_overloading_demo
A demo example of operator overloading in Python, implement elementary operations of complex number.  
  
1. Deine the 'Complex' calss. An Complex object can be instantiated by an argument have any type of `str` or a `tuple` of real&img parts value.  
2. Overloaing opretors of four fundamental rules `+-*/` by over-ridding some built-in methods.  
3. Several tests.  
```
c0=Complex('5-3i')
c1=c0+'4i'
print(c0,c1)
c1+=c0
print(c1)
c2=c1-c0
print(c2)
c3=c2*c0
print(c3)
c4=c3/c2
c4/=c1
print(c4)
c6=2/c1
print(c6)
c7=c6+c4*c3-c2+c1*4
print(c7)
c8=Complex((10,5))
print(c8)
```  
Out put:  
```
5.0-3.0i 5.0+1.0i
10.0-2.0i
5.0+1.0i
28.0-10.0i
0.10835798816568049-0.022559171597633137i
0.11538461538461539-0.019230769230769232i
37.923816568047336-10.734467455621303i
10.0+5.0i
```
