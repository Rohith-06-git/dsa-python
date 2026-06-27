class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_ind = (n + 1) // 2
        odd_ind = n // 2
        modulo = ( 10**9 ) + 7
        good_num = (pow( 5, even_ind, modulo) * pow( 4, odd_ind, modulo)) % modulo

        return good_num