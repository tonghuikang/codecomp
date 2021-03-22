#!/usr/bin/env python
# coding: utf-8

# # 1.bis. CBoW demo (Full text)
# 
# ### Imports

# In[1]:


import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import functools
import matplotlib.pyplot as plt
CUDA = torch.cuda.is_available()


# ### Step 1. Produce some data based on a given text for training our CBoW model    

# In[2]:


def text_to_train(text, context_window):
    
    # Get data from list of words in text, using a context window of size k = context_window
    data = []
    for i in range(context_window, len(text) - context_window):
        context = [text[i+e] for e in range(-context_window, context_window+1) if i+e != i]
        target = text[i]
        data.append((context, target))
        
    return data


# In[3]:


def create_text():
    
    # Load corpus from file
    with open("./text.txt", 'r', encoding="utf8",) as f:
        corpus = f.readlines()
    f.close()
    
    # Join corpus into a single string
    text = ""
    for s in corpus:
        l = s.split()
        for s2 in l:
            # Removes all special characters from string
            s2 = ''.join(filter(str.isalnum, s2))
            s2 += ' '
            text += s2.lower()
    text = text.split()
    
    return text


# In[4]:


text = create_text()
print(text)


# In[5]:


def generate_data(text, context_window):
    
    # Create vocabulary set V
    vocab = set(text)
    
    # Word to index and index 2 word converters
    word2index = {w:i for i,w in enumerate(vocab)}
    index2word = {i:w for i,w in enumerate(vocab)}
    
    # Generate data
    data = text_to_train(text, context_window)
    
    return vocab, data, word2index, index2word


# In[6]:


vocab, data, word2index, index2word = generate_data(text, context_window = 2)


# In[7]:


print(vocab)


# In[8]:


print(word2index)


# In[9]:


print(index2word)


# In[10]:


print(data)


# In[11]:


def words_to_tensor(words: list, w2i: dict, dtype = torch.FloatTensor):
    tensor =  dtype([w2i[word] for word in words])
    tensor = tensor.cuda()
    return Variable(tensor)


# ### Step 2. Create a CBoW model and train

# In[12]:


class CBOW(nn.Module):

    def __init__(self, context_size, embedding_size, vocab_size):
        super(CBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_size)
        self.linear = nn.Linear(embedding_size, vocab_size)

    def forward(self, inputs):
        lookup_embeds = self.embeddings(inputs)
        embeds = lookup_embeds.sum(dim=0)
        out = self.linear(embeds)
        #out = F.log_softmax(out, dim = -1)
        return out


# In[13]:


# Create model and pass to CUDA
model = CBOW(context_size = 2, embedding_size = 20, vocab_size = len(vocab))
model = model.cuda()
model.train()


# In[ ]:


# Define training parameters
learning_rate = 0.001
epochs = 1000
torch.manual_seed(28)
loss_func = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)


# In[ ]:


def get_prediction(context, model, word2index, index2word):
    
    # Get into eval() mode
    model.eval()
    ids = words_to_tensor(context, word2index, dtype = torch.LongTensor)
    
    # Forward pass
    prediction = model(ids)
    # Reshape to cover for absence of minibatches (needed for loss function)
    prediction = torch.reshape(prediction, (1, 467))
    _, index = torch.max(prediction, 1)
    
    return index2word[index.item()]


# In[ ]:


def check_accuracy(model, data, word2index, index2word):
    
    # Compute accuracy
    correct = 0
    for context, target in data:
        prediction = get_prediction(context, model, word2index, index2word)
        if prediction == target:
            correct += 1
            
    return correct/len(data)


# In[ ]:


losses = []
accuracies = []

for epoch in range(epochs):
    total_loss = 0
    
    for context, target in data:
        
        # Prepare data
        ids = words_to_tensor(context, word2index, dtype = torch.LongTensor)
        target = words_to_tensor([target], word2index, dtype = torch.LongTensor)
        
        # Forward pass
        model.zero_grad()
        output = model(ids)
        # Reshape to cover for absence of minibatches (needed for loss function)
        output = torch.reshape(output, (1, 467))
        loss = loss_func(output, target)
        
        # Backward pass and optim
        loss.backward()
        optimizer.step()
        
        # Loss update
        total_loss += loss.data.item()
    
    # Display
    if epoch % 10 == 0:
        accuracy = check_accuracy(model, data, word2index, index2word)
        print("Accuracy after epoch {} is {}".format(epoch, accuracy))
        accuracies.append(accuracy)
        losses.append(total_loss)


# ### 3. Visualization

# In[ ]:


# Display losses over time
plt.figure()
plt.plot(losses)
plt.show()


# In[ ]:


# Display accuracy over time
plt.figure()
plt.plot(accuracies)
plt.show()


# In[ ]:


word1 = words_to_tensor(["boys"], word2index, dtype = torch.LongTensor)
word2 = words_to_tensor(["brothers"], word2index, dtype = torch.LongTensor)
word3 = words_to_tensor(["dignity"], word2index, dtype = torch.LongTensor)
w1 = torch.reshape(model.embeddings(word1), (20,))
w2 = torch.reshape(model.embeddings(word2), (20,))
w3 = torch.reshape(model.embeddings(word3), (20,))
print(w1)
print(w2)
print(w3)

# Boys and Brothers have a somewhat close semantic meaning (strong positive value)
print(torch.dot(w1, w2).item())
# Boys and Dignity do not have a close semantic meaning (strong neg value)
print(torch.dot(w1, w3).item())


# In[14]:


if __name__ == "__main__":
    get_ipython().system('jupyter nbconvert --to script lung_dataset.ipynb')


# In[ ]:




