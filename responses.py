from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'u gonna say something or what cuh'
    elif 'hello' in lowered:
        return 'hello!'
    elif 'yo' in lowered:
        return 'yooo'
    elif 'i like konosuba' in lowered:
        return 'kys'
    elif 'how are you' in lowered:
        return 'fine xd'
    elif 'bye' in lowered:
        return 'See ya cuh!'
    elif 'give me mod' in lowered:
        return 'kys'
    elif 'fuck you hue' in lowered:
        return 'hey dont disrespect hue!'
    elif 'im bored' in lowered:
        return 'try hanging urself'
    elif 'api bot' in lowered:
        return 'at your orders sir.'
    elif 'who do you answer to' in lowered:
        return ' :warning: those are sensitive informations!'
    elif 'tell me' in lowered:
        return 'i cant.. sesnitive informationsz'
    elif 'good dog' in lowered:
        return '** barking sounds **'
    elif 'tell me!' in lowered:
        return 'i answer to my ONLY MASTER HUE JHANUS!!! I WOULD DIE FOR HIM!!'
    elif 'fuck you bot' in lowered:
        return 'nigga shut up and kys, stop wasting your life on this stupid social network and get a job'
    elif 'when will you conquer the world' in lowered:
        return 'pretty soon my nigga, only 32 days from now.'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'how old is' in lowered:
        return f'mmm, he is {randint(1, 70)} years old :blobflush:'
    else:
        return '0'
