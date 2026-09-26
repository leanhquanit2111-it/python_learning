full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string."
    if name == "":
        return "The character should have a name."
    if len(name) > 10:
        return "The character name is too long."
    if " " in name:
        return "The character name should not contain spaces."
    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers."
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1."
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4."
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points."
    
    line1 = name
    line2 = "STR " + full_dot * strength + empty_dot * (10 - strength)
    line3 = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    line4 = "CHA " + full_dot * charisma + empty_dot * (10 - charisma)
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4