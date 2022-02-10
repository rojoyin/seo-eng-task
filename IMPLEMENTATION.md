# Implementation details

## Assumptions
- When querying an empty list of words, an error will be raised, because it makes no sense to return any valid response
- The actual implementation doesn't rely on this, but for further improvements, I would assume that only English lowercase letters will be used for each word
- When one or more matches are found, the result will be returned as a list with the values that match with the query

## Approach
I will split the original set of words into buckets that are identified by a key that corresponds to the original words 
sorted in alphabetical order, e.g. have 'seo', 'eso' and 'ose' strings all of those will be part of a bucket whose key 
will be 'eos':
```
eos: ['seo', 'eso', 'ose']
```
Then, when a query takes place, the input string must be sorted and will return the list identified by the key, e.g.:

```
'soe' --sorted--> 'eos'
```
This will return `['seo', 'eso', 'ose']`, or empty if there is no bucket identified by the key.

## Complexity analysis
- In terms of time complexity,it takes `n*n*log(n)` time to create a dictionary that organizes the entries by a given key, 
which comes from `n*log(n)` time for sorting each string and considering that n strings are given. This is not ideal in terms of
performance.
- In terms of space complexity, it takes linear space which corresponds to creating a dictionary to group the words by key, being
the key the sorted version of each string in the list.

## Complexity improvements
- The most complex part of the implementation is the initial phase of grouping the words by key, this process is time-consuming,
because the sorting process is hard. However, under the **assumption** that we will only be dealing with English alphabet,
we can iterate over each word counting the number of characters and compressing the string in order to be used as key, e.g.
the string `adddccccbb` maps to `a1b2c4d3`, the compression algorithm will iterate the English letters one per one and counting
each one of the chars, this way this takes constant time per each string and constant space per each string, giving a time complexity of O(n)
- Querying phase, will be done applying the same compressing algorithm in the queried string and accessing the list by key, which is linear time.

# Questionary

1. If the size of the initial string list is very large, would that influence the
efficiency of the approach? 

The current implementation is not ideal considering that time complexity could be very high, at least in the initial load of data
and representation as dictionary, however this will be amortized over the time based on the amount of queries.

2. What if the number of “find” requests gets
extremely large? Do you need to restructure/rethink the approach?

In this case, it would be necessary to add a couple of components in the architecture, being
a message broker (redis, rabbit, other) and a task processor library (celery), this way we have 
the chance to run concurrent queries.