import json

def unpack(file):

    '''
    :param file: string to designate folder in a set path
    :return: None
    '''

    """
    unpack() unpacks the json output of twitter as it was output by the function collect_users()
    """

    with open(f'/data_users1/sagar/Euphoria-Project/{file}/responses.json', 'r') as f:
        txt = f.read()
        new_txt = txt.replace('}{', '},{')
        return json.loads(f'[{new_txt}]')