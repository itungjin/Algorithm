# 구현

N = int(input())
call_times = list(map(int, input().split()))

youngsik = 0
minsik = 0
for call_time in call_times:
    youngsik += ((call_time) // 30 + 1) * 10
    minsik += ((call_time) // 60 + 1) * 15

if youngsik < minsik:
    print('Y', youngsik)
elif youngsik > minsik:
    print('M', minsik)
else:
    print('Y', 'M', youngsik)
