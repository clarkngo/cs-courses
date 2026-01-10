import requests 
import unittest 
 
class FlaskTest(unittest.TestCase): 
 
   def test_1_postAPI(self): 
       url = "http://localhost:5000/students" 
 
       data = '{"name": "John","age": 32}' 
        
       headers = {"Content-Type": "application/json"} 
        
       # A POST request to the API 
       response = requests.post(url, data=data, headers=headers) 
 
       # Print the response 
       print(response.text) 
        
       # Test case result 
       self.assertEqual('Success', response.text) 
 
 
if __name__ == '__main__': 
   suite = unittest.TestLoader().loadTestsFromTestCase(FlaskTest) 
   testResult = unittest.TextTestRunner(verbosity=2).run(suite) 