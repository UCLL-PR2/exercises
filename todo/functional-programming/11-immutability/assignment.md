# Immutability

This series of exercises is named "functional programming".
But what exactly is this functional programming?
The exercises don't really give a clear picture.

Functional programming is revolves around _immutability_.
It is a programming style where one refrains from _modifying_ values.
Once a variable is assigned a value, we never change it.

The opposite of functional programming is called _imperative_ programming.
Imperative style allows values to be modified.

We give a few examples.

## Imperative vs Functional: Examples

Python offers two ways of sorting lists:

* We can use the method `lst.sort()`.
  Calling this method modifies `lst`: it moves the elements around so that `lst` ends up sorted.
  This is the _imperative_ approach.
  It's also referred to as _in place_ sorting.
* We can use the function `sorted(lst)`.
  In this case, `lst` remains unchanged.
  `sorted` returns a _new_ list which is the sorted version of `lst`.
  This is the _functional_ approach.

```python
# Imperative style: we modify xs
>>> lst = [4, 1, 3, 5, 2]
>>> lst.sort()
>>> lst
[1, 2, 3, 4, 5]

# Functional style
>>> lst = [4, 1, 3, 5, 2]
>>> sorted_lst = sorted(lst)
>>> lst
[4, 1, 3, 5, 2]

>>> sorted_lst
[1, 2, 3, 4, 5]
```

Note how after calling `lst.sort()`, the original order of the elements is forever lost.
This is why imperative operations are also called _destructive_.
It might be a bit strange to think of sorting as being destructive: all the elements are still there, are they not?
But imagine the list is a ranking of players and you then proceed to sort the list alphabetically on player names: you have then lost all ranking information.
Conversely, the functional approach is nondestructive: the original list still exists.

A similar pattern exists for reversing a list:

```python
# Imperative style
>>> lst = [1, 2, 3, 4, 5]
>>> lst.reverse()
>>> lst
[5, 4, 3, 2, 1]

# Functional style
>>> lst = [1, 2, 3, 4, 5]
>>> reversed_lst = reversed(lst)
>>> lst
[1, 2, 3, 4, 5]

>>> reversed_lst
[5, 4, 3, 2, 1]
```

Even though no information is lost (we can recover the original ordering by calling `reverse` as second time), `lst.reverse()` too is considered to be destructive due to it modifying `lst`.

## Functional Appending

If we are not allowed to make changes, how do we add an element to a list?
Surely that must still be possible somehow?

Here we present possible implementations of a function `append(lst, x)` that adds `x` to a `lst`.

```python
# Version 1: using list concatenation
def append(lst, x):
    return [lst] + [x]

# Version 2: using the * operator
def append(lst, x):
    return [*lst, x]
```

Note how these implementations leave `lst` unchanged but instead construct a _new_ list.

## Advantages

In essence, functional programming is the same as imperative programming, but without allowing modifications.
This feels like an arbitrary limitation.
Why would we want to restrict ourselves like that?

Before going into the actual reasons, we'd like to point out that functional programming is not just some weird academic idea that we decided to impose on you.
Functional programming has existed since the 1950's but has gained in relevance the last decade in the industry:

* In 2015, JavaScript was [extended](https://262.ecma-international.org/6.0/) with lambda functions (called arrow functions) and generators.
  It also provides higher order functions such as mapping, filtering, ...
* [Lambdas](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html) and [Streams](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html) were added to Java 8 (2014).
* Modern languages like [Swift](https://www.kodeco.com/books/swift-cookbook/v1.0/chapters/3-understand-variable-mutability-in-swift) (used to develop for iOS/MacOS), Kotlin (https://kotlinlang.org/docs/coding-conventions.html#immutability) (Java's successor) and Scala promote immutability.
* In [Rust](https://www.rust-lang.org/) (spiritual successor to C and C++), all variables are immutable by default unless otherwise specified.
* Lambdas were added to C++ in 2011.
* Libraries like Angular, ReactJS and Redux rely on objects being immutable.

### Complexity Reduction

Working with immutable objects tend to be much easier as there is no need to worry about modifications.
For example, `set`s only work with immutable values and `dict`s require keys to be immutable.
If mutable elements/keys were to be allowed, it would make the implementation of these data structures more complicated and performance would suffer.

A quick demonstration about how we can make `set`s fail:

```python
class Mutable:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return self.value


x = Mutable(0)

# We create a set with x in it
xs = {x}

# Obviously x is in xs
print(x in xs)         # prints True

# We modify x
x.value = 1

# x clearly should still be in xs
print(x in xs)         # prints False!

# We copy the contents of xs into a list
print(x in list(xs))   # prints True!
```

The inconsistent outputs are purely due to `set`s assumptions that elements do not change.

> This is not a Python specific problem: this problem can arise in all programming languages.

### Multithreading

Your CPU consists of multiple cores, each of which can run code in parallel.
Multithreading consists of designing your code in such a way that the work can be spread across multiple cores, thereby gaining a considerable speedup.

```python
from threading import Thread


def function():
  for i in range(100):
    print(i)

thread1 = Thread(target=function)
thread2 = Thread(target=function)
thread3 = Thread(target=function)

thread1.run()
thread2.run()
thread3.run()
```

In the code shown above, we create three _threads_.
Threads allow us to run functions in parallel.
It's as if you have assistants and give them orders to be executed while you're doing something else.
All three threads above execute the same code, i.e., each one will print the numbers from `0` to `99` in sequence.
However, there are no guarantees as to exactly when each thread will run.
The resulting output could be

* `0 0 0 1 1 1 2 2 2 3 3 3 ...`
* `0 1 2 3 ... 98 99 0 1 2 3 ... 98 99 0 1 2 3 ... 98 99`
* `0 1 0 1 0 1 2 3 2 3 2 3 ...`
* `0 1 2 3 4 5 0 1 0 1 2 6 2 3 7 3 8 4 5 ...`

There are actually 376523493564631064367712071965768747782444205128669798396168767743500485766630075466163294008566118208045715304490994009624725072511252178400 possible outputs for this very simple program, but typically only one of those outcomes is actually correct.
Please trust us when we say that writing multithreaded code is a _very_ complex endeavor.
On the one hand, you need to impose enough restrictions so that in the end, you always get the same result.
On the other hand, you cannot have too many restrictions lest you want performance to suffer and you end up with the same (or worse!) speed as a regular single threaded program.

Functional programming can dramatically reduce the complexity of parallel programming.
Without delving into technical details: functional programs naturally have only one possible outcome, while imperative programs tend to have exponentially many.
This is due to the fact that evaluation order has no impact on the result of functional programs.

### Distributed Systems

A multithreaded program utilizes multiple cores on your machine.
But what if you need that much processing power that a single machine won't do?

A [distributed system](https://en.wikipedia.org/wiki/Distributed_computing) makes use of multiple machines who communicate to each other using a network.
This adds even more complexity.

[Erlang](https://en.wikipedia.org/wiki/Erlang_(programming_language)) and [Elixir](https://en.wikipedia.org/wiki/Elixir_(programming_language)) are languages designed with distributed programming in mind.
As you can see on the linked pages, both mandate a functional programming style.

To understand the benefits of immutability, consider the following scenario.
Your application runs on two separate machines, let's call them A and B.
Both machines need access to the same object.
If this object were mutable, then each time A updates the object, it needs to notify B.
Conversely, every time B modifies the object, it needs to inform A.
This causes a lot of network traffic, which grows exponentially worse as more machines get involved.

However, if objects are known to be immutable, no such synchronization mechanism is necessary: A creates the object, sends all relevant information to B, and that's it.
A and B will forever agree on the object's state as it cannot change.

### Optimizations

Your code, whether it has been written in Python, JavaScript, C++, C#, Rust or any other programming languages, has to be translated to machine code, as this is the only language that your CPU can understand.
This translation (called _compilation_) only has to obey one rule: the generated machine code must _behave_ in the same way as your own code.

Many students believe translation is straightforward: "if I write `x += 1`, it will be translated into `ADD EAX, 1`."
This is not the case: the compiler (the software that performs the translation) is free to rewrite your code as it sees fit.
It will use this freedom to make your code run faster: it performs _optimizations_.

A very simple example would be

```python
result = 0
for i in range(10):
  result += i
```

An optimizing compiler would simply this to

```python
result = 10
```

In reality, optimizations go _much_ further than this: compilers can be quite smart these days and rewrite your code into something unrecognizable.
Also know that your CPU has all kinds of tricks ([branch prediction](https://en.wikipedia.org/wiki/Branch_predictor), [prefetching](https://en.wikipedia.org/wiki/Cache_prefetching), [pipelining](https://en.wikipedia.org/wiki/Instruction_pipelining), [out-of-order execution](https://en.wikipedia.org/wiki/Out-of-order_execution)) and instructions ([SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)) that the compiler can leverage to produce better performing code.

Functional programming allows more optimizations to be performed: the compiler can make additional assumptions (i.e., that values won't change) and use these to better optimize your program.

## Tasks

`starter.py` contains a series of functions written in imperative style: they all modify their arguments.
Rewrite them in functional style in `student.py`:

* Instead of modifying the argument, they must construct a new value and return it.
* Instead of using lists, use tuples, as these are basically immutable lists.
