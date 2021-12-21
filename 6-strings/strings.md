# Strings

- Optimize brute-force O(n) space to O(1) space
- String is immutable, use list if needed
- Write values to string from the back, if possible

## Snippets

1. Convert digit to string

```
chr(ord(0) + 7) // 7 -> "7"
```

2. Convert int to hex without `0x`

```
format(10, "x") // 10 -> a
format(10, "x") // 10 -> A
```
