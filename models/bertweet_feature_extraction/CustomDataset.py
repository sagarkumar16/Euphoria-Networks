import json
from torch.utils.data import Dataset


class CustomDataset(Dataset):

    def __init__(self,
                 file: 'filepath containing data in the form of a Twitter output json'):

        with open(file, 'r') as f:
            txt = f.read()
            new_txt = txt.replace('}{', '},{')

        self.tweets = json.loads(f'[{new_txt}]')

        data = list()

        for response in self.tweets:
            try:
                tweets = response['data']
                data.extend(tweets)
            except KeyError:
                pass

    '''
        ids = list()
        authors = list()
        text = list()

        for t in data:
            ids.append(t['id'])
            authors.append('author_id')
            text.append(t['text'])

        self.ids = ids
        self.authors = authors
        self.text = text
    '''

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def unpack(self):
        return self.data

