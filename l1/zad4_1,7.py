import struct

bity = "0" + "01111111" + "10110011001100110011001"
l_int = int(bity, 2)
war_float = struct.unpack(">f", l_int.to_bytes(4, byteorder="big"))[0]
war_dok = 1.7
b_bezwzgl = abs(war_dok - war_float)
b_wzgl = b_bezwzgl / abs(war_dok)

print(f"Wartość przybliżona: {war_float}")
print(f"Błąd bezwzględny: {b_bezwzgl}")
print(f"Błąd względny: {b_wzgl}")


