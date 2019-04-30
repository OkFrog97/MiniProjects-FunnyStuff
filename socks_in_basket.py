'''
Let's find same socks in basket with help of labda function.
basket is list of socks where same colors is a same numbers.
Example:
>basket = [10, 20, 30, 10]
>socks_finder(basket)
>1
>
>basket = [40,50,70,70,30,50]
>socks_finder(basket)
>2
>
>basket = [40. 20, 10]
>socks_finder(basket)
>0
>
'''

socks_finder=lambda basket: sum([basket.count(i)//2 for i in set(basket)])

def main ():
    basket = [10, 20, 30, 10]
    print(socks_finder(basket))
    basket = [40,50,70,70,30,50]
    print(socks_finder(basket))
    basket = [40, 20, 10]
    print(socks_finder(basket))
    
if __name__ == "__main__":
    main()
    