import re

# def getCurrentStamina(message):



# def extractDataRegex(pattern, replacement, string):


message = "🥔PEPE of Potato Castle\n"
message = message + "🏅Level: 13\n"
message = message + "⚔Atk: 26 🛡Def: 7\n"
message = message + "🔥Exp: 1321/1409\n"
message = message + "🔋Stamina: 5/8\n"
message = message + "💰Gold: 0\n"
message = message + "🤺PVP: 0\n"
message = message + "📚Expertise: -\n"
message = message + "\n"
message = message + "🎽Equipment +14⚔+5🛡:\n"
message = message + "Widow sword +10⚔\n"
message = message + "Steel dagger +3⚔\n"
message = message + "Leather shirt +4🛡\n"
message = message + "Royal Guard Cape +1⚔ +1🛡\n"
message = message + "\n"
message = message + "🎒Bag: 1/15 /inv\n"
message = message + "📦Warehouse: 180 /stock\n"

print(message)

print("REGEX:")

staminaRegex = "(.|\n)+^🔋Stamina: (\d+)/(\d+)(.|\n)+"

if re.search(staminaRegex, message, re.MULTILINE):
    print("MESSAGE HAS THE DATA")
else:
    print("WRONG MESSAGE (OR REGEX)")

newMessage = re.sub(staminaRegex, "Current Stamina: \\2 Max Stamina: \\3", message, 0, re.MULTILINE)


print(newMessage)



print("DONE")