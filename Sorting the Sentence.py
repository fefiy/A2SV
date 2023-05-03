def sortSentence(self, s: str):
     arrays = s.split(' ')
     arr = [None]*len(arrays)
     for i in range(len(arrays)):
         index= int (arrays[i][-1]) -1
         arr[index] = arrays[i][:-1]
        
      return (' '.join(arr))
