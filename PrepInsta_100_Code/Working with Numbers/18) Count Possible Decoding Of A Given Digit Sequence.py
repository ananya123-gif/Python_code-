# Count Possible Decoding Of A Given Digit Sequence

# Sequence = 131

# Possible decoding (1, 3, 1,)    = ACA
# Possible decoding (13, 1)   = MA
# So, the total possible decoding’s of sequence 131 is 2.

def cnt_decoding_digits(s):
    n=len(s)
    cnt = [0]*(n+1)
    cnt[0], cnt[1] = 1, 1

    for k in range(2,n+1):
        cnt[k] = 0
        cnt[k] = cnt[k-1]
        if s[k-2]=='1' or (s[k-2]=='2'and s[k-1]<'7'):
            cnt[k] += cnt[k-2]

    return cnt[n]

s = input()
print(cnt_decoding_digits(s))
