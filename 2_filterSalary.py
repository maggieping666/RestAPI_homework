import requests

url = 'http://dummy.restapiexample.com/api/v1/employees'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
response = requests.get(url, headers=headers)
employeeData = response.json().get('data')
print(employeeData)
for employee in employeeData:
    if int(employee['employee_salary']) >= 300000:
        print('id: '+employee['id'])
        print('Name: ' + employee['employee_name'])
        print('Age: '+employee['employee_age'])
        print("------------------------")



