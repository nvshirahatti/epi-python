# Linked Lists

- Singly: head, ...nodes, tail, null
- Doubly: self-loop
- Complexity: search O(n), insert O(1), delete O(1)
- Node: data, next
- Use exiting list nodes to reduce space complexity from O(n) to O(1)
- Use dummy head (sentinel) to avoid checking empty lists
- Update next for head and tail
- Use two iterators on singly: one ahead of the other / one faster than the other

## Snippets

1. Node

```python
class ListNode:
  def __init(self, data=0, next_node=None):
    self.data = data;
    self.next = next_node;
```

2. Search

```python
# O(n)
def search_list(L, key):
  while L and L.data != key:
    L = L.next
  return L
```

3. Insert

```python
# O(1)
def insert_after(node, new_node):
  new_node.next = node.next
  node.next = new_node
```

4. Delete

```python
# O(1)
def delete_after(node):
  node.next = node.next.next
```
