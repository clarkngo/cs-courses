print('What is your Math test score?')
score = int(input())

result = ""
if score < 75:
    result = "Failed"
elif score >= 80:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)