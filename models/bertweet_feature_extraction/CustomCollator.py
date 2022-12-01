import torch


class CustomCollator:

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def __call__(self, arr):
        X = [x['text'] for x in arr]

        enc = self.tokenizer(text=X, padding='longest', truncation=True, max_length=256)

        return torch.tensor(enc['input_ids']), torch.tensor(enc['attention_mask']), \
               torch.LongTensor([x['id'] for x in arr])