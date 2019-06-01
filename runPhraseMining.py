import phraseMining
import utils

print('Running Phrase Mining...')

file_name = "data.txt"
f = open(file_name)
input_string = ""
for line in f:
    input_string = line

# represents the minimum number of occurences you want each phrase to have.
min_support=1.5

# represents the threshold for merging two words into a phrase. A lower value
# alpha leads to higher recall and lower precision,
alpha=5

# length of the maximum phrase size
max_phrase_size=10

phrase_miner = phraseMining.PhraseMining(input_string, min_support, max_phrase_size, alpha);
partitioned_docs, index_vocab = phrase_miner.mine()
frequent_phrases = phrase_miner.get_frequent_phrases(min_support)

utils.store_partitioned_docs(partitioned_docs)
utils.store_vocab(index_vocab)
utils.store_frequent_phrases(frequent_phrases)