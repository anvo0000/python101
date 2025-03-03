### Raise my Own Error
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 2:
    raise ValueError(f"Human height should not be over 2 meters.")
bmi = weight / (height **2)
print(bmi)