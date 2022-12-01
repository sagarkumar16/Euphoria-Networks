from FeatureExtraction import FeatureExtraction
import argparse
import torch
import os
import numpy as np


def main():

    print('pid: ', os.getpid())

    parser = argparse.ArgumentParser()

    ## ARGUMENTS ##

    parser.add_argument("--feature_extraction",
                        action='store_true',
                        default=True,
                        help='Runs feature extraction using transformers library model.')

    parser.add_argument("--file",
                        type=str,
                        help='Filepath for the json file of tweets.')

    parser.add_argument("--outfile",
                        type=str,
                        help='Filepath for pickle where results are stored as .npy files. no file extension needed.')

    parser.add_argument("--transformer_model",
                        type=str,
                        default='vinai/bertweet-base',
                        help='Choice of pretrained model (must be part of transformers package). Default is BERTweet.'
                        )

    # END OF ARGPARSE #

    args = parser.parse_args()

    seed_val = args.seed
    random.seed(seed_val)
    np.random.seed(seed_val)
    torch.manual_seed(seed_val)

    torch.cuda.manual_seed_all(seed_val)

    if args.feature_extraction:

        bertweet = FeatureExtraction(file=args.file)

        embeddings = bertweet()

        np.save(args.outfile + '.npy', embeddings)

    return

if __name__ == '__main__':
    main()