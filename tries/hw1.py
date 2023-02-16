"""
HW 1: Tries

Name: Jana Hayaly

PennKey: jhayaly

Number of hours spent on homework: 3

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.
"""


def add_word(trie, word):
    """
    Add a word to the given trie.

    Args:
        trie (dict): the dictionary representation of a trie
        word (str): the word to be added

    Returns:
        None

    Side effect:
        trie is modified with word included
    """
    # start the search at the root of the trie
    cur_node = trie
    for c in word: # iterate over characters c in word/prefix
        if c not in cur_node: # perform logic at cur_node
            cur_node[c] = {}
        # move to the next node in the trie
        cur_node = cur_node[c]


def create_trie(word_list):
    """
    Creates a trie from the given word list.

    Hint: use your completed implementation of add_word()

    Args:
        word_list (list): list of words (str)

    Returns:
        dict: a dictionary representation of the trie
    """
    trie = {}
    for word in word_list:
        add_word(trie, word)
    return trie



def in_trie(trie, word):
    """
    Check whether the given word is present within the trie.

    Args:
        word (str): the word to check
        trie (dict): the trie to check against

    Returns:
        bool: True if the word is in the trie, False if it is not
    """    

    curr = trie
    for c in word: # iterate over characters c in word/prefix
        if c not in curr: # perform logic at cur_node
            return False
        else:
            curr = curr[c]
    return curr == {}

def list_matches(trie, prefix):
    
    """List all word with the given prefix in the trie.
    If no words in the trie match the given prefix, return an empty list.

    Hint: you may want to write a recursive helper function to traverse the
    trie.

    Args:
        prefix (str): the prefix to match against
        trie (dict): the trie to search over

    Returns:
        list: all words in the trie that begin with prefix"""

    curr = trie
    for c in prefix: # iterate over characters c in word/prefix
        if c not in curr: # perform logic at cur_node
            print('no words with this prefix')
            return []
        else:
            curr = curr[c]
    
    og_list = []
    list_return_helper(curr, prefix, og_list)
    return og_list
    

def list_return_helper(curr, word, list):
    if curr == {}:
        list.append(word)
        #return list
    else:
        for key in curr: 
            list_return_helper(curr[key], word + key, list)
        # iterate through trie and store words 
    


# for testing purposes- please ignore :)
def main():
    """main function"""
    word_list = ['bear']
    """my_trie = {}
    add_word(my_trie, 'hi')
    add_word(my_trie, 'bye')
    add_word(my_trie, 'hello')
    print(my_trie)
    my_trie = create_trie(word_list)
    print(my_trie)
    print(in_trie(my_trie, 'bear'))
    print(in_trie(my_trie, 'bye'))"""

    gs_word_list = ['car', 'cat']
    gs_trie = create_trie(gs_word_list)
    print(in_trie(gs_trie, ''))
    print(in_trie(gs_trie, 'ca'))
    print(in_trie(gs_trie, 'c'))
    print(in_trie(gs_trie, 'cat'))
    print(in_trie(gs_trie, 'car'))

    """word_list_other = ['bear', 'dog', 'cat', 'car']
    my_other_trie = create_trie(word_list_other)
    print(my_other_trie)
    print(in_trie(my_other_trie, 'dgo'))

    yet_another_list = ['donut', 'dog', 'cat', 'dot']
    yet_another_trie = create_trie(yet_another_list)
    print(yet_another_trie)
    
    #print(list_return_helper(my_trie,'',[]))
    #print(list_return_helper(my_other_trie, '',[]))
    #print(list_return_helper(yet_another_trie, '', []))
    # only prints the last starting node word
    
    list = list_matches(my_trie, 'be')
    print(list)
    
    print(list_matches(my_other_trie, 'pi'))
    #yet_another_list = ['donut', 'dog', 'cat', 'dot']
    #yet_another_trie = create_trie(yet_another_list)
    #print(yet_another_trie)
    print(list_matches(yet_another_trie, 'do'))"""


if __name__ == '__main__':
    """
    Feel free to test your implementation here by running python3 hw1.py in
    your terminal
    """
    main()