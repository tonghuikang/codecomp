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
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# ### Step 1. Data Processing

# In[2]:


k = 1  # window size
testcase = "f1"


# In[3]:


with open(testcase, "r") as f:
    sentences = [[int(x) for x in sentence.strip().split()] for sentence in f.readlines()][1:]
sentences = [[-2]*k + sentence + [-2]*k for sentence in sentences]
sentences = [[x%1024 for x in sentence] for sentence in sentences]

VOCAB_SIZE = 1024  # actually 1000+2


# In[4]:


data = []
for sentence in sentences:
    for segment in zip(*[sentence[i:] for i in range(2*k+1)]):
#         if c == 1023:
#             continue
        data.append([[*segment[:k], *segment[-k:]], segment[k]])
print(len(data))


# In[5]:


test_data = []
for sentence in sentences:
    for segment in zip(*[sentence[i:] for i in range(2*k+1)]):
        if segment[k] == 1023:
            test_data.append([*segment[:k], *segment[-k:]])
print(len(test_data))


# ### Step 2. Create a CBoW model and train

# In[6]:


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


# In[7]:


# Create model and pass to CUDA
model = CBOW(context_size = 2, embedding_size = 20, vocab_size = VOCAB_SIZE)
model = model.to(device)
model.train()


# In[8]:


# Define training parameters
learning_rate = 0.001
epochs = 10
torch.manual_seed(28)
loss_func = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)


# In[9]:


def measure_accuracy(model):
    model.eval()
    num_correct = 0
    num_data = 0
    for context, target in data:
        if target > 1000:
            continue
        ids = torch.tensor(context)
        output = model(ids)
        result = torch.argmax(output[:-2]).item()
        
        num_data += 1
        if result == target:
            num_correct += 1
    return num_correct/num_data


# In[ ]:


losses = []
accuracies = []

model.train()
for epoch in range(epochs):
    total_loss = 0
    
    for context, target in data:
        
        # Prepare data
        ids = torch.tensor(context)
        target = torch.tensor([target])
                
        # Forward pass
        model.zero_grad()
        output = model(ids)
        # Reshape to cover for absence of minibatches (needed for loss function)
        output = torch.reshape(output, (1, VOCAB_SIZE))
        loss = loss_func(output, target)
        
        # Backward pass and optim
        loss.backward()
        optimizer.step()
        
        # Loss update
        total_loss += loss.data.item()
        
    accuracies.append(measure_accuracy(model))
    losses.append(total_loss)
    print(epoch, end=" ")


# In[ ]:


model.eval()
results = []
for context in test_data:
    ids = torch.tensor(context)
    output = model(ids)
    result = torch.argmax(output[:-2]).item()  # exclude -1 (mask) and -2 (end)
    results.append(result)


# In[ ]:


with open("{}.cbow".format(testcase), "w") as f:
    f.write("\n".join([str(result) for result in results]))


# ### 3. Visualization

# In[ ]:


# Display losses over time
plt.figure()
plt.plot(losses)
plt.show()


# In[ ]:


# Display losses over time
plt.figure()
plt.plot(accuracies)
plt.show()


# In[ ]:


if __name__ == "__main__":
    get_ipython().system('jupyter nbconvert --to script cbow.ipynb')


# In[ ]:





# In[ ]:




