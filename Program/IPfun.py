def CausalConv(array1, array2, time):
    """
        Evaluate convolution for two causal functions.
        >>Input
        array1: array for fun1(t) 
        array2: array for fun2(t)
        time: array for time
        
        .. math::
        
            Out(t) = \int_{0}^{t} fun1(a) fun2(t-a) da
            
    """
    
    if array1.shape == array2.shape == time.shape:
        out = np.convolve(array1, array2)
        return out[0:size(time)]*(time[1]-time[0])
    else:
        print "Give me same size of 1D arrays!!"

def TriangleFun(time, ta, tb):
    """
        .. math::

            I(t) = \frac{1}{t_a}t, 0 < t \le t_a

            I(t) = -\frac{1}{t_b-t_a}(t-t_b), t_a < t < t_b

            I(t) = 0, t \le t_a or t \ge t_b    

    """
    out = np.zeros(time.size)
    out[time<=ta] = 1/ta*time[time<=ta]
    out[(time>ta)&(time<tb)] = -1/(tb-ta)*(time[(time>ta)&(time<tb)]-tb)
    return out


def VTEMFun(time, ta, tb, a):
    """
        .. math::

        I(t) = \frac{1}{1-e^{-a}}(1-e^{-a\frac{t}{t_a}}), 0 < t \le t_a

        I(t) = -\frac{1}{t_b-t_a}(t-t_b), t_a < t < t_b

        I(t) = 0, t \le t_a or t \ge t_b
    """
    out = np.zeros(time.size)
    out[time<=ta] = (1-np.exp(-a*time[time<=ta]/ta))/(1-np.exp(-a))
    out[(time>ta)&(time<tb)] = -1/(tb-ta)*(time[(time>ta)&(time<tb)]-tb)
    return out


def RectFun(time, ta, tb):
    """
        .. math::

        I(t) = 1, 0 < t \le t_a

        I(t) = -1, t_a < t < t_b

        I(t) = 0, t \le t_a or t \ge t_b
    """    
    out = np.zeros(time.size)
    out[time<=ta] = 1
    out[(time>ta)&(time<tb)] = -1
    return out