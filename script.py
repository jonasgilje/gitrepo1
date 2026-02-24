import pandas

series1 = pandas.Series([1, 3, 5, 7])
series2 = pandas.Series(["a", "b", "c", "d"])

print(series1)
print(series2)

print("Endring 3")

print("Endring 4")
print("""Endring 5 etter endring 4
      Dette vil bli en konflikt
      """)

print(series1 * 3)
