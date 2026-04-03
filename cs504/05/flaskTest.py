import requests
import unittest

class FlaskTest(unittest.TestCase):

    def test_1_postAPI (self): 
        url = "http://127.0.0.1:5000/students"
 
         
        data='{"name": "John","age": 32}' 
         
        headers = {"Content-Type": "application/json"} 
         
        # A POST  request to the API 
        response = requests.post(url,data=data,headers=headers) 
        # Print the response 
         
        print(response.text) 
         
        # Test case result 
        self.assertEqual('Success', response.text) 
  
 
        def test_2_getAPI(self): 
            url = "http://127.0.0.1:5000/students/John" 

            
            # A GET request to the API 
            response = requests.get(url) 
            # Print the response 
            
            print(response.text) 
            
            # Test case result 
            self.assertEqual('Record Found John age is 32', response.text)
if __name__ == '__main__': 
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskTest) 
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)