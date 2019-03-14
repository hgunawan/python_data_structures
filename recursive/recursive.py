from timeit import default_timer as timer



def get_fib(position):
    if position <= 1:
       return position
    # print('fib1 called with', position)
    n = get_fib(position - 1) + get_fib(position - 2) 
    return n
        
        

# Test cases
# print(get_fib(6))

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def get_fib_memo(position, memo={}):    
    if position in memo:
        ans = memo[position]
    elif position <= 2:
        ans = 1
        memo[position] = ans
    else:
        ans = get_fib_memo(position - 2) + get_fib_memo(position - 1)
        memo[position] = ans

    # print(position)
    return ans

print(get_fib_memo(80))


def fib(n):
    def accFib(n, Nm2=0, Nm1=1):
        for i in range(n):
            Nm2, Nm1 = Nm1, Nm1+Nm2
        return Nm2   
    return accFib(n)

start = timer()
print(get_fib_memo(80))
end = timer()
print(end - start)


start = timer()
print(fib(80))
end = timer()
print(end - start)