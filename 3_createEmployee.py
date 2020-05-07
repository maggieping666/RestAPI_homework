import requests
import unittest


class TestCases(unittest.TestCase):
    post_url = 'http://dummy.restapiexample.com/api/v1/create'
    get_url = 'http://dummy.restapiexample.com/api/v1/employees'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    data = {"name": "Tester", "salary": "54321", "age": "30"}

    def test_create_employee(self):
        self.post_resp = requests.post(self.post_url, json=self.data, headers=self.headers)
        print("Result after post:")
        print(self.post_resp.json())
        self.assertEqual('success', self.post_resp.json().get('status'), "Failed to create an employee")
        employee_id = self.post_resp.json().get('data')['id']
        '''Get employees after post'''
        self.get_resp = requests.get(self.get_url, headers=self.headers)
        print("Get employees after create:")
        print(self.get_resp.json())
        id_array = []
        for employee in self.get_resp.json().get('data'):
            id_array.append(employee['id'])

        self.assertIn(employee_id, id_array, "New created employee can't be found")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()





