class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        sys.set_int_max_str_digits(10**6)
       
        s = 1
        for i in range(left, right + 1):
            s *= i

        count = 0
        while s % 10 == 0:
            s //= 10
            count += 1

        s = str(s)

        if len(s) > 10:
            prefix = s[:5]
            suffix = s[-5:]
            return f"{prefix}...{suffix}e{count}"
        else:
            return f"{s}e{count}"