#!/usr/bin/env python
# coding: utf-8

# # 1.bis. CBoW demo (Full text)
# 
# ### Imports

# In[52]:


import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import functools
import matplotlib.pyplot as plt
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# ### Step 1. Data Processing

# In[53]:


with open("f0", "r") as f:
    sentences = [[int(x) for x in sentence.strip().split()] for sentence in f.readlines()][1:]
sentences = [[-2]*2 + sentence + [-2]*2 for sentence in sentences]
sentences = [[x%1024 for x in sentence] for sentence in sentences]

VOCAB_SIZE = 1024


# In[54]:


# k = 2
data = []
for sentence in sentences:
    for a,b,c,d,e in zip(*[sentence[i:] for i in range(5)]):
#         if c == 1023:
#             continue
        data.append([[a,b,d,e], c])
print(len(data))


# In[55]:


test_data = []
for sentence in sentences:
    for a,b,c,d,e in zip(*[sentence[i:] for i in range(5)]):
        if c == 1023:
            test_data.append([a,b,d,e])
print(len(test_data))


# ### Step 2. Create a CBoW model and train

# In[56]:


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


# In[57]:


# Create model and pass to CUDA
model = CBOW(context_size = 2, embedding_size = 20, vocab_size = VOCAB_SIZE)
model = model.to(device)
model.train()


# In[62]:


# Define training parameters
learning_rate = 0.001
epochs = 2
torch.manual_seed(28)
loss_func = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)


# In[63]:


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
    losses.append(total_loss)
    print(epoch, end=" ")


# In[64]:


model.eval()
results = []
for context in test_data:
    ids = torch.tensor(context)
    output = model(ids)
    result = torch.argmax(output[:-2]).item()  # exclude -1 (mask) and -2 (end)
    results.append(result)


# In[65]:


with open("f0.cbow", "w") as f:
    f.write("\n".join([str(result) for result in results]))


# ### 3. Visualization

# In[43]:


# Display losses over time
plt.figure()
plt.plot(losses)
plt.show()


# In[39]:


if __name__ == "__main__":
    get_ipython().system('jupyter nbconvert --to script cbow.ipynb')


# In[ ]:




