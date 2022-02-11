# O(nlogn) time | O(1) space
def eliminate_duplicates(A):
    A.sort(key=lambda a: a[0])
    write_i = 1
    for a in A[1:]:
        if a[0] != A[write_i - 1][0]:
            A[write_i] = a
            write_i += 1
    del A[write_i:]


if __name__ == "__main__":
    A = [("Ian", "Botham"), ("David", "Gower"), ("Ian", "Chappel")]
    eliminate_duplicates(A)
    assert A == [("David", "Gower"), ("Ian", "Botham")]
    print("All tests passed!")
