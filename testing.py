import unittest

class StatsList(list):
    def mean(self):
        return sum(self)/len(self)
    
    def median(self):
        if len(self) % 2:
            return self[int(len(self)/2)]
        else:
            idx = int(len(self)/2)
            return(self[idx] + self[idx - 1])/2
            
class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1,1.0)

if __name__ == "__main__":
    unittest.main()
