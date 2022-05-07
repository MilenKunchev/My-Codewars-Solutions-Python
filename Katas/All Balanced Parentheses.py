def balanced_parens(n):
    def generateParenthesis(n, Open, close, s, ans):
        if (Open == n and close == n):
            ans.append(s)
            return

        if (Open < n):
            generateParenthesis(n, Open + 1, close, s + "(", ans)

        if (close < Open):
            generateParenthesis(n, Open, close + 1, s + ")", ans)

    ans = []

    generateParenthesis(n, 0, 0, "", ans)
    return ans



# print(balanced_parens(0))  # => [""]
# print(balanced_parens(1))  # => ["()"]
# print(balanced_parens(2))  # => ["()()","(())"]
print(balanced_parens(3))  # => ["()()()","(())()","()(())","(()())","((()))"]
print(balanced_parens(4))  # => ["()()()","(())()","()(())","(()())","((()))"]
