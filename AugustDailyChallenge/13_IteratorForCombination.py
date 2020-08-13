Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

Solution:

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.i = 0
        self.finalResult = []
        self.combine('', 0)
    
    def combine(self, string, start):
        if len(string) == self.combinationLength:
            self.finalResult.append(string)
            return
        else:
            for i in range(start, len(self.characters)):
                self.combine(string + self.characters[i], i+1)

    def next(self) -> str:
        finalResult = self.finalResult[self.i]
        self.i += 1
        return finalResult

    def hasNext(self) -> bool:
        return self.i < len(self.finalResult)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
