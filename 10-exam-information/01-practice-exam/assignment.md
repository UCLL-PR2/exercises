# File System Exercise

* Place all code for this exercise in `filesystem.py`.
* In these instructions we will always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure to get the names exactly right, even those of the parameters.
* A missing class will cause tests focusing on that class to be skipped.
  Skipped tests therefore still count as failed.
* The tests only perform superficial checks.
  Failing/skipped tests means that your code is definitely incomplete or incorrect.
  But passing tests does not mean that your code is fully correct!

## Storage Device

A `StorageDevice` (like an SSD or USB drive) consists of a number of equally sized blocks.
For example, a `StorageDevice` could have 100 blocks, each with size 5MB:

```python
>>> storage = StorageDevice(block_count=100, block_size=5 * BYTES_PER_MEGABYTE)
```

Blocks are represented by numbers going from `0` to `block_count - 1`.
For example, if a storage device has 5 blocks, its blocks are `0`, `1`, `2`, `3` and `4`.

Initially, all blocks are available.
Later on, we will add files that need blocks to store their contents.
A `StorageDevice` keeps track of which blocks are available and which ones are in use.
Used blocks can also be freed, making them available again.

```python
>>> storage = StorageDevice(block_count=10, block_size=5)
# available blocks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# used blocks: []

>>> storage.block_size
5

>>> storage.total_block_count
10

# Initially, all blocks are available...
>>> storage.available_block_count
10

# ...and no blocks are in use
>>> storage.used_block_count
0
```

A storage device has two operations:

* `allocate(block_count)` allocates `block_count` blocks and returns them in a list.
  The `StorageDevice` registers these blocks as being used.
* `free(blocks)` marks the given blocks as being available again.

```python
>>> storage = StorageDevice(block_count=10, block_size=5)
# available blocks: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# used blocks: []

>>> storage.allocate(3)
[0, 1, 2]
# available blocks: [3, 4, 5, 6, 7, 8, 9]
# used blocks: [0, 1, 2]

>>> storage.allocate(5)
[3, 4, 5, 6, 7]
# available blocks: [8, 9]
# used blocks: [0, 1, 2, 3, 4, 5, 6, 7]

>>> storage.free([2, 3, 4])
# available blocks: [2, 3, 4, 8, 9]
# used blocks: [0, 1, 5, 6, 7]

# Cannot free blocks that are not in use
>>> storage.free([9])
RuntimeError
```

* Define a class `StorageDevice`.
* Define its constructor.
  * It should have two parameters: `block_count` and `block_size`.
  * In a *private* field `available_blocks`, it stores a set containing the numbers `0` to `block_count` (exclusive).
  * In a *private* field `used_blocks`, it stores an empty set.
  * It stores the block size in a *private* field `block_size`.
* Add a public property `available_block_count` which returns the number of available blocks.
* Add a public property `used_block_count` which returns the number of used blocks.
* Add a public property `total_block_count` which returns the total number of blocks (both available and used).
* Add a public property `block_size` which returns the size of the blocks.
* Define a public method `allocate`.
  * It has a parameter  `block_count` (an integer).
  * The method takes `block_count` available blocks from `available_blocks` and returns them as a list.
        It also moves these blocks from `available_blocks` to `used_blocks`.
        Note: in order to take N blocks from `available_blocks`, it might be helpful to first convert it into a list.
  * If there are insufficient available blocks left, a `RuntimeError` is raised.
* Define a public method `free`.
  * It has a parameter `blocks` (a list of block indices).
  * Only used blocks can be freed.
        If `blocks` contains blocks that do not appear in the `used_blocks`, none of the blocks are freed and a `RuntimeError` is raised.
  * The method adds the given blocks to `available_blocks` and removes them from `used_blocks`.

## File System

A file system contains two kinds of "entities": files and directories.
We will represent them in Python using the classes `File` and `Directory`.
Since they have functionality in common, we also introduce a class `Entity` that will contain these shared members.

### `Entity`

An `Entity` has a name and keeps track of the `StorageDevice` it is stored on.
An `Entity`'s name has to obey certain rules:

* The name can only contain letters (both upper and lower are permitted), digits and dots.
* The name must have at least 1 character and be no longer than 16 characters.

* Define an abstract class `Entity`.
* Define a static method `is_valid_name(name)` that returns `True` if `name` is valid and `False` otherwise.
* Define a constructor for `Entity`.
  * It has two parameters: `storage` (a `StorageDevice` object) and `name` (a string).
  * It must store both these values in private fields.
  * It must raise a `RuntimeError` in case the given `name` is invalid.
* Define a property `name`.
  * It must have a getter, i.e., `entity.name` must return the `Entity`'s name.
  * It must have a setter, i.e., `entity.name = new_name` must update the `Entity`'s name.
  * The setter must raise a `RuntimeError` in case the new name is invalid.
* Define a readonly property `storage` that returns the `StorageDevice` the `Entity` is stored on.
* Define a readonly abstract property `size_in_blocks`.
* Define a readonly property `size_in_bytes` that returns the size of the `Entity` in bytes.
      This is done by multiplying the `Entity`'s `size_in_blocks` by the `StorageDevice`'s `block_size`.
* Define an abstract method `clear()`.
      It takes no parameters.

### `File`

A `File` inherits from `Entity`.
Aside from a name and storage device (inherited from `Entity`), a `File` also keeps track of the list of blocks it occupies on its storage device.
At creation, a `File` is empty.
It can be made to grow using `file.grow(block_count)`, which causes it to allocate `block_count` blocks from its associated `StorageDevice`.
Clearing a file resets the file's size back to zero, returning all blocks to the `StorageDevice`.

Example Usage:

```python
>>> my_ssd = StorageDevice(block_count=10, block_size=4096)

# Create a file named 'filename.txt'
>>> file = File(storage=my_ssd, filename='filename.txt')


# Getting file's name
>>> file.name
'filename.txt'

# Changing file's name
>>> file.name = 'newname.txt'
>>> file.name
'newname.txt'

# Trying to set an invalid name
>>> file.name = 'invalid name'
RuntimeError


# We allocate 8 blocks of storage for this file
>>> file.grow(block_count=8)

# Getting the size in blocks
>>> file.size_in_blocks
8

# Storage has 8 fewer blocks available
>>> storage.available_block_count
2

>>> storage.used_block_count
8


# Computing its size in bytes (= number of blocks used * block_size of storage)
>>> file.size_in_bytes
32768


# Clearing file resets its size to 0
>>> file.clear()
>>> file.size_in_blocks
0

# Storage has been freed
>>> storage.available_block_count
10

>>> storage.used_block_count
0
```

* Define a class `File`.
* It inherits from `Entity`.
* Define `File`'s constructor.
  * The constructor takes two parameters: `storage` and `name`.
  * It relies on `Entity`'s constructor to initialize its `storage` and `name`.
  * A freshly created `File` is empty and therefore occupies zero blocks of storage.
* Define a method `grow(block_count)` which allocates an extra `block_count` blocks from its storage.
      These extra blocks must also be kept track of.
* Define a readonly property `size_in_blocks` which returns the number of blocks occupied by the `File`.
* Define the method `clear()`.
      It returns all of the blocks the `File` occupies to the `StorageDevice` (using `free`).
      After `clear()`, the `File` is empty.

### `Directory`

A `Directory` is a kind of `Entity`. It therefore inherits `name` and `storage`.
Just like real directories, a `Directory` can contain other files and directories.
Put more formally, a `Directory` keeps track of a list of "children".
Initially, a `Directory` is empty, i.e., it has zero children.
Children can be added using `add(child)`.

Clearing a directory means all files it contains are cleared recursively:

* All direct `File` children must be cleared.
* If a `Directory` contains subdirectories, then the `File`s in those subdirectories must also be cleared.
* The same happens for subdirectories of subdirectories, etc.

Example usage:

```python
>>> my_ssd = StorageDevice(block_count=1000, block_size=4096)
>>> directory = Directory(storage=my_ssd, name='myfolder')

# Initially, a directory takes no room
>>> directory.size_in_blocks
0

# We add a file
>>> file1 = File(my_ssd, 'file1')
>>> file1.grow(5)
>>> directory.add(file1)

# The directory's size is the sum of all of its children's sizes
>>> directory.size_in_blocks
5

# We add a second file
>>> file2 = File(my_ssd, 'file2')
>>> file2.grow(10)
>>> directory.add(file2)
>>> directory.size_in_blocks
15

# We create a subdirectory and add a file to it
>>> subdir = Directory(my_ssd, 'subdir')
>>> directory.add(subdir)
>>> file3 = File(my_ssd, 'file3')
>>> file3.grow(20)
>>> subdir.add(file3)

# The directory's size has grown
>>> directory.size_in_blocks
35

# All files are cleared recursively
>>> directory.clear()
>>> directory.size_in_blocks
0

>>> file1.size_in_blocks
0

>>> file2.size_in_blocks
0

>>> file3.size_in_blocks
0
```

* Define a class `Directory`.
* It inherits from `Entity`.
* Define `Directory`'s constructor.
  * The constructor takes two parameters: `storage` and `name`.
  * It relies on `Entity`'s constructor to initialize its `storage` and `name`.
  * A freshly created `Directory` is empty and starts with an empty list of `children`.
* Define a method `add(entity)` that adds the given `entity` (which can be either a `File` or a `Directory`) to the list of `children`.
* Define a property `size_in_blocks` that computes the total size of the `Directory`.
      The size of a `Directory` is defined as the sum of the sizes of all its `children`.
* Define a method `clear()` that clears all files recursively, as described above.