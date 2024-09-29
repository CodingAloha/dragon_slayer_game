"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
gradeToTest = 99
if gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90:
    print("A")
elif gradeToTest >= 80:
    print("B")
elif gradeToTest >= 70:
    print("C")
elif gradeToTest >= 50:
    print("D")
else:
    print("F")