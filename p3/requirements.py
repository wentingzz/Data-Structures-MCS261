# Feel free to comment out these lines before your algorithms are implemented.
from zip_tree import ZipTree

# Details about Gradescope submission:

# - No file should include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - The submission should either be the files themselves, or a zip file not containing any directories.


# Explanations for ZipTree public member functions

# any variable annotated with KeyType should use the same type for each tree, and should be comparable.
# ValType is for any additional data to be stored in the nodes.
# get_random_rank(): returns a random node rank, chosen independently from a geometric distribution of mean 1.
# insert(): inserts item with parameter key, value, and rank into tree.
#           if rank is not provided, a random rank should be selected by using ZipTree.get_random_rank().
# remove(): removes item with parameter key from tree.
#           you can assume that the item exists in the tree.
# find(): returns the value of item with parameter key.
#         you can assume that the item exists in the tree.
# get_size(): returns the number of nodes in the tree.
# get_height(): returns the height of the tree.
# get_depth(): returns the depth of the item with parameter key.
#              you can assume that the item exists in the tree.

