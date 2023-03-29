# Replacing the Head

Write a function `nth(linked_list, index)` that returns the value of the node with the given `index`.
You can assume `linked_list` contains enough elements.

Start with an imperative solution, then write a recursive one.

## Hint (Recursive)

Implementing `nth` is about skipping `Node`s.
Take it upon yourself to skip one `Node` and have someone else (= recursive call) skip the remaining nodes.
