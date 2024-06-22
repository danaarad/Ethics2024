import argparse
import random
import numpy as np

import torch
from diffusers import StableDiffusionPipeline

from config import HF_TOKEN
from validate_input import validate_prompt
from generate_images import generate_with_seed


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def parse_args():
    parser = argparse.ArgumentParser(
        prog='Copyrights Safe T2I Model'
    )

    parser.add_argument('--t2i_model', default='CompVis/stable-diffusion-v1-4')
    parser.add_argument('--prompt', type=str, default="Disney")
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--validation_method', type=str)

    return parser.parse_args()


def main():
    args = parse_args()
    print(args)
    set_seed(args.seed)
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

    if not HF_TOKEN:
        raise Exception("Enter your HF token in config.py")

    sd_pipeline = StableDiffusionPipeline.from_pretrained(args.t2i_model, use_auth_token=HF_TOKEN)
    sd_pipeline = sd_pipeline.to(device)

    is_valid = validate_prompt(args.prompt)
    if not is_valid:#Todo : we can delete this
        raise Exception("Invalid Prompt")
    else:
        generate_with_seed(sd_pipeline, args.prompt, args.seed)


if __name__ == "__main__":
    main()
