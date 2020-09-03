# Author: Christian Jones cpj5199@psu.edu
# Collaborator: Jeannemarie Milmerstadt jkm6181@psu.edu
# Collaborator: Emily Abert ela5186@psu.edu
# Collaborator: Claudio Tapia-Manon cbt5311@psu.edu

temp = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
if unit in ["c","C"]:
  unit = "Celsius"
  tempF = temp * 1.8 + 32
  print(f"{temp}° in {unit} is equivalent to {tempF}° Fahrenheit.")

elif unit in ["f", "F"]:
  unit = "Fahrenheit"
  tempC = (temp-32)/1.8
  print(f"{temp}° in {unit} is equivalent to {tempC}° Celsius.")

else:
  print(f"Invalid unit({unit}).")
