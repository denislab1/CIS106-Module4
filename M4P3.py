meal = float(input("Enter meal total: "))

tip15 = meal * 0.15
tip18 = meal * 0.18
tip20 = meal * 0.20

print("\nWith 15% Tip:")
print(f"Total: {meal:.2f}")
print(f"Tip: {tip15:.2f}")
print(f"Total with Tip: {meal + tip15:.2f}")

print("\nWith 18% Tip:")
print(f"Total: {meal:.2f}")
print(f"Tip: {tip18:.2f}")
print(f"Total with Tip: {meal + tip18:.2f}")

print("\nWith 20% Tip:")
print(f"Total: {meal:.2f}")
print(f"Tip: {tip20:.2f}")
print(f"Total with Tip: {meal + tip20:.2f}")