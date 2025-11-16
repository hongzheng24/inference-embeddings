#!/bin/bash

#SBATCH -p gpu --gres=gpu:2
#SBATCH -n 4
#SBATCH -t 48:00:00
#SBATCH --mem=16G
#SBATCH -J JobInferenceEmbeddings
#SBATCH -o JobInferenceEmbeddings-%j.out
#SBATCH -e JobInferenceEmbeddings-%j.out

export PYTHONUNBUFFERED=TRUE

python ~/data/hzheng29/inference_embeddings/main.py