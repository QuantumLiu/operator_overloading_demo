# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:54:17 2017

@author: Quantum Liu
"""
import re

P_IM=r'([-+]?[0-9]*\.?[0-9]*)i[+-]*?'
P_REAL=r'([-+]?[0-9]*\.?[0-9]*)[^i]'
class Complex():
    def __init__(self,ri_pair=()):
        if isinstance(ri_pair,(tuple,list)):
            if len(ri_pair)==1:
                assert isinstance(ri_pair[0],(int,float))
                self.real_num,self.real_str,self.im_num,self.im_str=float(ri_pair[0]),str(float(ri_pair[0])),0.0,'0.0'
            elif len(ri_pair)==2:
                assert all(map(lambda s:isinstance(s,(int,float)),ri_pair))
                self.real_num,self.real_str,self.im_num,self.im_str=float(ri_pair[0]),str(float(ri_pair[0])),float(ri_pair[1]),str(float(ri_pair[1]))
            else:
                raise ValueError('ri_pair must be a tuple or list that has two numbers!')
        else:
            if isinstance(ri_pair,(int,float)):
                self=Complex(ri_pair=(ri_pair,0))
            elif isinstance(ri_pair,str):
                self.x=re.sub(r'[^\d+-i]','',ri_pair)#Sub meaning less chars.
                self.im_str,self.real_str=re.findall(P_IM,self.x)[0],re.findall(P_REAL,self.x)[0]
                if not self.im_str:
                    self.im_num=0
                else:
                    self.im_num=float(self.im_str)
                if not self.real_str:
                    self.real_num=0
                else:
                    self.real_num=float(self.real_str)
            else:
                raise TypeError('atgument x must be a number or str')
        self.__radd__=self.__add__
        self.__rsub__=self.__sub__
        self.__rmul__=self.__mul__
    def _covertinst(self,x):
        '''
        类型转换
        '''
        if isinstance(x,str):
            cpx=Complex(x)
        elif isinstance(x,(float,int)):
            cpx=Complex(ri_pair=(x,))
        elif isinstance(x,tuple):
            cpx==Complex(ri_pair=x)
        elif isinstance(x,Complex):
            cpx=x
        else:
            raise ValueError('x must be a str or a Complex object')
        return cpx
    
    def __add__(self,x):
        '''
        重载+
        '''
        cpx=self._covertinst(x)
        return Complex(ri_pair=(self.real_num+cpx.real_num,self.im_num+cpx.im_num))
    
    def __sub__(self,x):
        '''
        重载-
        '''
        cpx=self._covertinst(x)
        return Complex(ri_pair=(self.real_num-cpx.real_num,self.im_num-cpx.im_num))
        
    def __mul__(self,x):
        '''
        重载*
        '''
        cpx=self._covertinst(x)
        return Complex(ri_pair=(self.real_num*cpx.real_num-self.im_num*cpx.im_num,self.im_num*cpx.real_num+self.real_num*cpx.im_num))

    def __truediv__(self,x):
        '''
        重载/
        '''
        cpx=self._covertinst(x)
        m=self.__add__(cpx)
        d=cpx.real_num**2+cpx.im_num**2
        return Complex(ri_pair=(m.real_num/d,m.im_num/d))
    
    def __rtruediv__(self,x):
        '''
        右除
        '''
        cpx=self._covertinst(x)
        return cpx/self
    
    def __repr__(self):
        '''
        重载print
        '''
        sym=('+' if self.im_num>=0 else '')
        return '{r}{sym}{i}i'.format(r=self.real_num,sym=sym,i=self.im_num)
if __name__=='__main__':
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
