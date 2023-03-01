# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
gplayer_1 = "Ruud Gullit"
gplayer_2 = "Marco van Basten"
goal_1 =  32
goal_2 = 54
scorers = gplayer_1 + ' ' + str(goal_1) + ', ' + gplayer_2 + ' ' + str(goal_2)

# check if code works as intended
print(scorers)

#f-string 
report = f"{gplayer_1} scored in the {goal_1}nd minute \n{gplayer_2} scored in the {goal_2}nd minute"

#check if code works as intended
print(report)

#first_name
#  using split (but not find, but seems easier)
#player = "Frank Rijkaard"
#first_name = player.split(" ")[0]

#solution using find and slicing
player = "Frank Rijkaard"
first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find(' ') + 1:])
name_short = player[0] + ". " + player[player.find(' ') + 1:]
chant = ((first_name + "! ") * len(first_name))[:-1]
print(chant[-1] != " ")

#check to see if everything works
print(player, first_name, last_name_len, name_short, chant)