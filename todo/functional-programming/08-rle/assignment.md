# RLE

[Run Length Encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE) is a very simple compression algorithm.
Say we have the string `'aaaaaaaabbbbbcccccccc'`.
It consists of

* 8 `a`'s
* 5 `b`'s
* 7 `c`'s

This sums up to 20 bytes.
We can rewrite this as `[('a', 8), ('b', 5), ('c' 7)]`, which amounts to 6 bytes of data.
(Admittedly we do make some simplifications, but we don't want to get into the gnarly technical details.)

Even though our rewritten form is much more compact, no information is lost: given only `[('a', 8), ('b', 5), ('c' 7)]`, we can reconstruct the original string exactly.

No compression algorithm is perfect though: there will always be inputs for which "compression" will actually _increase_ the size of your file.
In the case of RLE, this occurs when there are no runs of the same character.
If we apply RLE on `'abcde'`, we would get `[('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)]`, which is double the size of the original!
In other words, RLE only works well on very specific kinds of inputs, which is why it's not often used (fax machines do use it for example.)

## Tasks

Write a _generator_ function `rle_encode(data)` with the following specifications:

* The parameter `data` can be an iterable or an iterator.
  (This shouldn't add any extra complexity to your code.)
* `data` is a sequence of chars, i.e., strings of length 1.
* `rle_encode` should return an iterator that produces pairs `(char, count)` as explained above.

Write a _generator_ function `rle_decode(data)`:

* The parameter `data` can be an iterable or an iterator.
  (This shouldn't add any extra complexity to your code.)
* `data` is a sequence of pairs `(char, count)`.
* `rle_decode` should return an iterator that produces chars (strings of length one.)

`rle_decode(rle_encode(data))` should generate the same characters as in `data`.
