
minus (x:xs) (y:ys) = case (compare x y) of
           LT -> x : minus xs (y:ys)
           EQ ->     minus xs ys
           GT ->     minus (x:xs) ys
minus xs _ = xs

maxPossible = 775147

numberToFactor :: Int
numberToFactor = maxPossible


possiblePrimeList :: Int -> [Int]
possiblePrimeList x = [2..x]

--primeSieve :: [Integer] -> [Integer] -> [Integer]
--primeSieve [] primeList = primeList
--primeSieve uncheckedList primeList = primeSieve (filter (\x -> (mod x (head uncheckedList)) /= 0) (tail uncheckedList)) (primeList ++ [(head uncheckedList)])
primesToQ :: Int -> [Int]
primesToQ m = 2 : sieve [3,5..m] where
    sieve [] = []
    sieve (p:xs) = p : sieve (xs `minus ` [p*p, p*p+2*p..m])
--primeSieve (p:xs)

--possiblePrimes :: Integer -> [Integer]
--possiblePrimes x = primeSieve (possiblePrimeList x) []

defaultPossiblePrimes :: [Int]
--defaultPossiblePrimes = possiblePrimes maxPrime
defaultPossiblePrimes = primesToQ numberToFactor

primeFactors :: [Int] -> Int -> [Int] -> [Int]
primeFactors [] n ys = ys
primeFactors (x:xs) n ys
    | (x*x) > n = ys
    | (mod n x) == 0 = (primeFactors (x:xs) (floor n/x) (ys ++ x))
    | otherwise = primeFactors xs n ys

maxPrimes = maximum defaultPossiblePrimes

main :: IO()
main = putStrLn (show maxPrimes)
