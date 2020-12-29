#https://www.youtube.com/watch?v=D3GDFfCOLss&ab_channel=TheWonderSeven
#O(m*n*k)
#O(1)
#kmp ultimately......
def isWinner(codeList,shoppingCart):
    m, n = len(shoppingCart), len(codeList)
    if n <= 0 :
        return 1
    counter = 0
    i = 0
    for code in codeList:
        while i < m:
            j = 0
            while j < len(code) and i+j < m:
                if (code[j] == shoppingCart[i+j]) or (code[j] == 'anything'):
                    j += 1
                else:
                    break
            if j == len(code):
                counter += 1
                i += j
                break
            else:
                i += 1
    return 1 if counter == n else 0
#test case:
#expect 1
print(isWinner([['apple','apple'],['banana','anything','banana']],['apple','apple','banana','orange','banana']))
#expect 0
print(isWinner([['apple','apple'],['banana','anything','banana']],['banana','orange','banana','apple','apple']))
#expect 0 
print(isWinner([['apple','apple'],['banana','anything','banana']],['apple','banana','apple','banana','orange','banana']))
#expect 0
print(isWinner([['apple','apple'],['apple','apple','banana']],['apple','apple','apple','banana']))
#expect 1
print(isWinner([['apple','apple'],['banana','anything','banana']],['apple','apple','orange','banana','orange','banana']))
#expect 1
print(isWinner([['anything','apple'],['anything','anything','banana']],['orange','apple','orange','apple','orange','banana']))
