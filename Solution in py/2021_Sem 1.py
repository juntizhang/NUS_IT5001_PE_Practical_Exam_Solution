''' 2021 Sem 1'''
## Part 1 DNA Comparison (15 + 15 = 30 marks)
### Task 1 Iterative DNA Comparison (15 marks)
def compareDNA_I(dna1,dna2):
    res = ''
    for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
            res += '*'
        else:
            res += '.'
    return res

### Task 2 Recursive Run-length Decoding (15 marks)
def compareDNA_R(dna1,dna2):
    if not dna1:
        return ''
    elif dna1[0] == dna2[0]:
        dna1 = '*'+compareDNA_R(dna1[1:],dna2[1:])
    else:
        dna1 = '.'+compareDNA_R(dna1[1:],dna2[1:])
    return dna1

## Part 2 Local Peaks Searching (15+15+10 = 35 marks)
### Task 1 Array Version (15 marks)
def local_peak_array_version(survey):
    survey = [-1] + survey + [-1]
    for i in range(1,len(survey)):
        if survey[i-1] < survey[i] > survey[i+1]:
            return i-1
    
local_peak_array_version([4,5,2,7,8,2,1,2,3,4,8])

### Task 2 Function Version (15 marks)

# This method cannot deal with large inputs
def local_peak_function_version(a,b,survey):
    lst = [-1]+[survey(i) for i in range(a,b+1)]+[-1]
    for i in range(1,len(lst)):
        if lst[i-1] < lst[i] > lst[i+1]:
            return i+a-1
survey3 = lambda i: [1,2,3,4,5,6,5,4,3,2][i%10]
print(local_peak_function_version(11,19,survey3))

### Important!! Binary sort!
def local_peak_function_version(a,b,survey):
    # Set for the starting and ending points
    if survey(a) > survey(a+1): return a        
    elif survey(b) > survey(b-1): return b
    # Other points in between
    while b - a > 2:
        if survey((a+b)//2) > survey((a+b)//2+1):
            b = (a+b)//2 + 1
        else:
            a = (a+b)//2
    if survey(a) >= survey(b):
        return a + 1
    else:
        return b + 1
survey2 = lambda i: i if i <= 1234567890 else (1234567890*2) - i - 1
print(local_peak_function_version(0,12345678900,survey2))

## Part 3 Fibonacci Password (10+20= 30 marks)
### Task 1 The nth Password (10 marks)

# This recursion version cannot deal with large inputs
def nth_day_pw(N):
    if N < 1: return ''
    elif N == 1: return 'F'
    elif N == 2: return 'B'
    else :  
        return nth_day_pw(N-2) + nth_day_pw(N-1)

# lARGE INPUT Version
def nth_day_pw(N):
    if N == 1: return 'F'
    elif N == 2: return 'B'
    res,previous_res1,previous_res2 = 'FB','F','B'
    n = 3
    while n < N:
        previous_res1 = previous_res2
        previous_res2 = res
        res = previous_res1 + previous_res2
        n += 1
    return res
nth_day_pw(40)[-20:]

### Task 2 The kth Letter of the nth Day Password(20 marks)
def kth_letter_nth_day_pw(k,n) :
    def fib_len(n): # Return the length of the nth password
        if n == 1 or n == 2: return 1
        res,previous_res1,previous_res2 = 2,1,1
        k = 3
        while k < n:
            previous_res1 = previous_res2
            previous_res2 = res
            res = previous_res1 + previous_res2
            k += 1
        return res
    while n > 4: # Since the kth character always remain the same after 3th word
        prev_len = fib_len(n-1)
        if k <= prev_len:
            n -= 1
        else:
            k = k - fib_len(n-2)
            n -= 1
    if k == 1 or k == 3: return 'B'
    elif k == 2: return 'F'
print(kth_letter_nth_day_pw(12345,999))