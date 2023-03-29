def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print(i*i)
    print(l)
f(2)
f(3)

# [] is a mutable object, it retains its state from the previous function call that's why f(2)'s [0, 1] were added in output of f(3)