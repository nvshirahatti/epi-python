# Chapter 14. Binary Search Tree

- BST is workhorse of data structures
- Efficient in searchhing, finding min and max, looking up successor or predecessor of a search key, and enumerating keys in sorted order
- Red-black tree is height-balanced BST
- Avoid putting mutable objects in BST
- Otherwise, to update mutable object in BST, always remove it first, update it, and add it back

Operations O(logn) time

- Find min and max elements
- Find next largest/next smallest element
- Lookup, delete, and find

- Traverse takes O(h) time, h: height of tree
- Iterate in sorted order takes O(n) time regardless of tree is balanced

- Some problems need a combination of BST and hashtable
- Sometimes, it's necessary to **augment** BST to manipulated complicated data, i.e. intervals
- BST property is global -> No idea!

`sortedcontainers` and `bintrees`

`bintrees`:

- insert(e): insert new
- discard(e): remove e if present
- min_item()/max_item(): yield smallest/largest key-value pair
- min_key()/max_key(): yield smallest/largest key
- pop_min()/pop_max(): remove and return smallest/largest key-value pair
