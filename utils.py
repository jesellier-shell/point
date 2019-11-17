class StepFunction1D:
    
    def __init__(self, time, values) :
        self.time = time
        self.values = values
        
    def value(self, T) :
        
        for (t, v) in zip(self.time, self.values):
            if(T < t):
                return v
            
        return self.values[-1]
        
    def integral(self, T):
        
        cumul = 0
        prev_t = 0
        
        for (t, v) in zip(self.time, self.values):
            if(T < t):
                return cumul + (T-prev_t)*v
            
            cumul = cumul + (t-prev_t)*v
            prev_t = t
        
        cumul = cumul + (T-prev_t)*v
        return cumul

        

