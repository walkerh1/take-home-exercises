# take-home-exercises

## Q1
Solution to this problem runs in O(nlogn) time. It uses python's built-in sorted() function, and defines a custom comparator.

To run Q1, type the following command into the command-line:
```
$ python3 q1.py
```
Then enter a value n for the number of elements in the array. Then enter, one at a time, the n numbers to sort. The sorted array will then be printed to stdout, one number per line.

## Q2
Solution to this is more complex. I first observe that this problem is equivalent to finding the sequence m(1), m(2), m(3),..., m(n) where m(i) <= i for all 0 <= i <= n, such that the cumulative sum sequence, cs(m), corresponding to the sequence m, satisfies the following:
- the unlucky number, k, does not appear anywhere as a term in cs(m), and
- the last term in cs(m) is greater than or equal to the last term of the cumulative sum sequence corresponding to every other sequence m' that satisfies (i). (i.e. cs(m) results in the max amount of money amongst all the sequences that satisfy the unlucky number constraint.)

Given this we can prove the following: for any number of students, n, and any unlucky number, k, the maximum amount of money, maxMoney, that can be collected must be either:
1. <pre>n*(n+1)/2   (a)</pre>
2. <pre>(n*(n+1)/2) - 1   (b)</pre>

To prove this I show that if maxMoney is not equal to (a), then it must be equal to (b). So suppose it is not equal to (a). Then the cumulative sum sequence,
- <pre>1, 3, 6, ... , n*(n+1)/2   (*)</pre>
corresponding to the sequence 1, 2, 3,..., n (i.e. the result of taking all the money from every classmate), must contain k exactly once somewhere in it. So the next largest possible value of maxMoney is (n*(n+1)/2) - 1, and this is the final term of the cumulative sum sequence,
- <pre>0, 2, 5, ... , (n*(n+1)/2) - 1   (**)</pre>
corresponding to the sequence 0, 2, 3,..., n (i.e. the result of taking 0 dollars from the first classmate and everything from every other classmate). And this doesn't contain k anywhere in it. To see why, note that if k appears in sequence (\*), then k-1 must appear in sequence (\*\*). So if k did appear in (\*\*), then we would have both k-1 and k occur in it. But because each term in (\*\*) is strictly greater than 1 plus the preceding term, it is impossible for k-1 and k to both occur in (\*\*). Therefore, k does not appear in (\*\*), and so maxMoney must be equal to its last term, namely (b).

Given this, we can come up with quite a simple algorithm to solve the problem. Just run through the sequence 1, 2, 3, ... , n, keeping track of the cumulative sum. If this sum ever equals the unlucky number, return value (b). Otherwise return value (a). This algorithm runs in O(n) time.

But it turns out we can do better!

What we need to know is whether, given some n and k, there is some i <= n such that:
<pre>k = i*(i+1)/2</pre>
We can rearrange this equation to get:
<pre>0 = i^2 + i - 2k</pre>
Then to solve for i > 0, we can apply the usual formula for solving quadratics, which simplifies to:
<pre>i = (-1 + sqrt(1 + 8k))/2</pre>
This will return some i>0. All we then need to do is check firstly whether i is an integer, and secondly whether i <= n (note that we always have i > 0 if k > 0). If it satisfies both these conditions, then the unlucky number is encountered during the collection of money, and so we return the value (b) above. If not, the unlucky number is not encountered, and we return the value (a). This algorithm runs in O(1) time and uses O(1) space.

To run Q2, type the following command into the command-line:
```
$ python3 q2.py
```
Then enter a value n, and then enter a value for k. The result will be then be printed to stdout.

## Tests

To run the tests enter the following on the command-line:
```
$ python3 q1_tests.py
$ python3 q2_tests.py
```
and the test scripts will run, showing a pass or fail result.
