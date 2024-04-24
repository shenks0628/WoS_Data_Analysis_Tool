# from transformers import BertTokenizer, BertModel
# import torch

# # Load the pre-trained BERT model and tokenizer
# model_name = 'bert-base-uncased'
# tokenizer = BertTokenizer.from_pretrained(model_name)
# model = BertModel.from_pretrained(model_name)

# # Define a list of words
# # word_list = ['apple', 'banana', 'orange', 'car', 'truck', 'bus']
# # word_list = ['cars', 'trucks', 'buses', 'car', 'truck', 'bus', 'leaf']
# # word_list = ['high', 'low']
# word_list = ['like', 'love', 'hate', 'adore']
# # word_list = ['autonomous vehicles', 'autonomous driving', 'autonomous aerial vehicles', 'autonomous vehicle',
# #              'safety', 'lidar', 'radar', 'sensors', 'autonomous underwater vehicle', 'navigation',
# #              'collision avoidance', 'roads', 'reinforcement learning', 'uav', 'object detection', 'machine learning']

# # Tokenize the words
# tokens = tokenizer(word_list, padding=True, truncation=True, return_tensors='pt')

# # Pass the tokenized input through the BERT model
# outputs = model(**tokens)

# # Get the embeddings for each word
# embeddings = outputs.last_hidden_state

# print(embeddings)

# # Calculate the similarities between each word
# similarity_matrix = torch.cosine_similarity(embeddings.unsqueeze(1), embeddings.unsqueeze(0), dim=2)

# similarity_matrix = similarity_matrix.detach().numpy()

# # Print the similarity matrix
# print(similarity_matrix)

# # Print the similarity scores
# with open('output_similarity.txt', 'w') as file:
#     for i, word in enumerate(word_list):
#         for j, word2 in enumerate(word_list):
#             if i < j:
#                 print(f'Similarity between "{word}" and "{word2}": {similarity_matrix[i][j].mean()}', file=file)

import spacy
from scipy.spatial.distance import cosine

# Load an English word embedding model
nlp = spacy.load('en_core_web_lg')

# word_list = ['autonomous vehicles', 'autonomous driving', 'autonomous aerial vehicles', 'autonomous vehicle',
#              'safety', 'lidar', 'radar', 'sensors', 'autonomous underwater vehicle', 'navigation',
#              'collision avoidance', 'roads', 'reinforcement learning', 'uav', 'object detection', 'machine learning']

# read the word list from the output.txt
word_list = []
cnt = 0
with open('output.txt', 'r') as file:
    for line in file:
        # find the last index of '('
        idx = line.rfind('(')
        # remove the bracket and the number
        line = line[:idx]
        cnt += 1
        word_list.append(line.strip())
        if cnt >= 100:
            break

words = [nlp(word) for word in word_list]

# Calculate the similarities between each word
with open('output_similarity.txt', 'w') as file:
    for i, s in enumerate(words):
        for j, t in enumerate(words):
            if i < j and s.similarity(t) > 0.8:
                print(f'Similarity between "{s}" and "{t}": {s.similarity(t)}', file=file)