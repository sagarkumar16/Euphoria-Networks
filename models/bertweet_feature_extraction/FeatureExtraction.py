import os
import json
import torch
import numpy as np
from transformers import AutoModel, AutoTokenizer
from torch.utils.data import DataLoader
import sys
sys.path.append(".")
from CustomDataset import CustomDataset



class FeatureExtraction:

    def __init__(self,
                 file: 'filepath containing data in the form of a Twitter output json',
                 model: "transformers model to use" = None):

        self.file = file
        self.model = model

    def __call__(self):

        tokenizer = AutoTokenizer.from_pretrained(self.model, use_fast=False)
        collator_fn = CustomCollator(tokenizer=tokenizer)

        dataset = CustomDataset(file=self.file)
        loader = DataLoader(dataset, batch_size=16, shuffle=False, num_workers=1, collate_fn=collator_fn)

        if torch.cuda.is_visible():

            device = torch.device('cuda')

            bertweet = AutoModel.from_pretrained(self.model)

        else:
            print("CUDA not available. Running on CPU.")

            device = torch.device('cuda')

            bertweet = AutoModel.from_pretrained(self.model)

        pbar = tqdm(loader)

        embeddings = dict()

        with torch.no_grad():

            for tup in pbar:
                X, masks, ids = tup[0].to(device), tup[1].to(device), tup[2].to(device)
                features = bertweet(input_ids=X, attention_masks=masks)
                embeddings[ids] = features.last_hidden_state[:,0,:]

        return np.array(embeddings)







