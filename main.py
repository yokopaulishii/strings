# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_a = 'Ruud Gullit'
scorer_b = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_a  + ' ' + str(goal_0) + ',' + ' ' + scorer_b + ' ' + str(goal_1)
report = scorer_a + ' '+ 'scored in the' + ' ' + str(goal_0) + 'nd minute' + '\n' + scorer_b + ' ' + 'scored in the' + ' ' + str(goal_1) + 'th minute'
formatting_scorer_a = f'{scorer_a} scored in the {goal_0}nd minute'
formatting_scorer_b = f'{scorer_b} scored in the {goal_1}th minute'
player = 'Ruud Gullit'
spatie_index = player.find(' ') 
first_name = player[:spatie_index] 
last_name = player[spatie_index+1:11]
last_name_len = len(player[5:11])
name_s = player[:1]
name_short = name_s + '.' + ' ' + last_name
a = first_name + '! '
x = len(player[0:4])
b = a*x
chant = b[:-1] 
good_chant = chant[-1] != ' '
