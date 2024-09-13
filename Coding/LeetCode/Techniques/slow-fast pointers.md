```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) : return False
        if not s : return True

        s_p = 0

        for i in range(len(t)) :
            if t[i] == s[s_p] :
                s_p += 1
                if s_p == len(s) : return True
            
        return False
```

Referring to one of the questions [[392. Is Subsequence]], this is one use case.
We iterate one pointer, but the other pointer would be slower (relatively).
And that pointer would only proceed/decrement based on a certain condition (required by the question).