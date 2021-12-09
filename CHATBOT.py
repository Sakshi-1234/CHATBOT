import random

var_1=['hi','hello']
var_2=['how are you','how are you doing','how is your health']
var_3=['what is your nam','how do I call you','name','your name please']
var_4=['programming language','what should I learn']
var_5=['what are your hobbies','hobbies','what do you do in free time']

while True:
    user_input=input('Sakhi said to bot: ')

    if user_input.lower() in var_1:
        bot_1=['hello','hi']
        print('Bot replied to sakshi: '+random.choice(bot_1)+'\n')
    elif user_input.lower() in var_2:
        bot_2=['I am good','I am doing good','I am fine']
        print('Bot replied to sakshi: '+random.choice(bot_2)+'\n')
    elif user_input.lower() in var_3:
        bot_3=['My name is chatterbot','call me chatterbot','chatterbot','My name is chatterbot']
        print('Bot replied to sakshi: '+random.choice(bot_3)+'\n')
    elif user_input.lower() in var_4:
        bot_4=['python','python programming']
        print('Bot replied to sakshi: '+random.choice(bot_4)+'\n')
    elif user_input.lower() in var_5:
        bot_5=['learning a programming','learning a programming language','learn a programming language']
        print('Bot replied to sakshi: '+random.choice(bot_5)+'\n')
    else:
        print('Bot replied to sakshi-sorry ehat are you asking,I am not getting that?'+'\n')
        
    
