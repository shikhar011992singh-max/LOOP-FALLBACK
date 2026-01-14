flavours =["Ginger","out of stock","lemon","discontinued","tulsi"]

for flavour in flavours:
      if flavour == "Out of Stock":
            continue
      if flavour == "Discontinued":
         print(f"{flavour}item found")
         break
      print(f"{flavour}item found")

print(f"outside of loop")     