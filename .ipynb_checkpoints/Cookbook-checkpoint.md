## Count Words

```python
>>> freq_dic = {}
>>> for text in ftexts:
...     words = tokenizer.tokenize(text)
...     for word in words:
...         # form dictionary
...         try:
...             freq_dic[word] += 1
...         except:
...             freq_dic[word] = 1
```

```python

```
