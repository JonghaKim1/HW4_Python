def allcaps(Fn): 
    def Wrapper(): 
        String = Fn();
        Result = String.upper();
        return Result;
    return Wrapper;