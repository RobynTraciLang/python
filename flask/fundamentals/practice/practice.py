praise_team = {
    "sopranos": ["Robyn", "Carolyn", "Ryan", "Danielle"],
    "altos": ["Kirsten", "Alana", "Yasmin", "Rachel", "Joyce"],
    "tenors":["Therry", "Randel", "Ayitey", "Shedria", "Ohimai"],
}

print(praise_team.keys())
print(praise_team.values())
print(praise_team.items())

for key in praise_team.keys():
    print(key)

for val in praise_team.values():
    print(val)

for key, val in praise_team.items():
    print(val)
    print(key)
    print(f"{key}: {val}")

praise_team["sopranos"].append = "Imani"
print(praise_team["sopranos"])

