# Hash Tables

- Key - value
- O(1): insert, delete, lookup

- HT stores keys in an array
- A key is stored in array locations (slots) based on its "hash code"
- Hash code: integer computed from key by hash function

- 2 keys map to same location, collision occurs
- Solution to collision: linked list

## Libraries

set, dict, collections.defaultdict, collections.Counter
