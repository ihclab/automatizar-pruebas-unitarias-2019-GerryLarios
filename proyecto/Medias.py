class Media(object):

    def aritmetica(self, vals):
        '''Calcula y regresa la media artimética'''
        s = 0
        for item in vals:
            s = s + item
        
        return s / len(vals)
    
    def geometrica(self, vals):
        '''Calcula y regresa la media geométrica'''
        m = 1
        for item in vals:
            m = m * item
            
        return pow(m, 1 / len(vals))
    
    def armonica(self, vals):
        '''Calcula y regresa la media armonica'''
        s = 0
        for item in vals:
            s = s + (1 / item)
        return len(vals) / s
    
    # def _raiz(self, x, n):
    #     pass
    