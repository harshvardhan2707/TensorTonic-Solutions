import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        for i, val in enumerate([self.pad_token, self.unk_token, self.bos_token, self.eos_token]):
            self.word_to_id[val] = i
            self.id_to_word[i] = val
        
        tot_words = []

        for text in texts:
            for word in text.lower().split():
                if word not in tot_words:
                    tot_words.append(word)
        
        tot_words.sort()

        for word in tot_words:
            i+=1
            self.word_to_id[word] = i
            self.id_to_word[i] = word

        self.vocab_size = i+1
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        ans = []
        for word in text.lower().split():
            ans.append(self.word_to_id.get(word,1))
        return ans
            
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        ans = []
        for id in ids:
            print(self.id_to_word)
            ans.append(self.id_to_word.get(id, "<UNK>"))
        return " ".join(ans)
