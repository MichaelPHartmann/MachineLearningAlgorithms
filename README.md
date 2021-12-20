# Machine Learning Algorithms
# From Scratch in Python

### WHY?
I needed to brush up on my machine learning algorithm theory and the best way to learn is by doing, so I decided to write some popular algos.

I'm building them all from scratch because using something like scikit doesn't really help you understand the mechanics of algorithms. I learn best by understanding the inner workings of things, I think it's huge in developing an intuitive understanding the process.

Learn the micro to understand the macro.

### HOW?
I want the code to be as free from external libraries as possible, even if there are time and space optimisations. Being able to look at the code and see exactly what's happening is much more valuable in this circumstance.

There are some exceptions to this rule. The first is for data visualisation, it's not core to the function of any of the algos, and is mostly for debugging. The second is certain math functions. While it's easy to implement these by hand, they are more easily readable and don't detract from understanding the inner workings. That said I still wrote many from scratch. The third is unit testing. I could just litter a module with try/excepts and assert statements, but getting used to unittest seemed valuable, and it simplifies things a bit.

### WHAT?
These algorithms aren't meant to be pretty, they're primarily a learning excercise.
The documentation will be inconsistent and sparse, but the bones of the algo should be there.

Right now I have implemented the following algorithms:

- K Nearest Neighbour
- Weighted K Nearest Neighbour
- Single Variable Linear Regression
- Multiple Variable Linear Regression

On my list of algorithms to explore:

- Decision Trees
- Logistic Regression
- Naive Bayes
- PCA Techniques
- ICA Techniques
