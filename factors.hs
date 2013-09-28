
minus (x:xs) (y:ys) = case (compare x y) of
           LT -> x : minus xs (y:ys)
           EQ ->     minus xs ys
           GT ->     minus (x:xs) ys
minus xs _ = xs

possiblePrimeList :: Integer -> [Integer]
possiblePrimeList x = [2..x]

primesToQ :: Integer -> [Integer]
primesToQ m = 2 : sieve [3,5..m] where
    sieve [] = []
    sieve (p:xs) = p : sieve (xs `minus ` [p*p, p*p+2*p..m])


defaultPossiblePrimes :: Integer -> [Integer]
defaultPossiblePrimes numberToFactor = primesToQ numberToFactor

primeFactors :: [Integer] -> Integer -> [Integer] -> [Integer]
primeFactors [] n ys = ys
primeFactors (x:xs) n ys
    | (mod n x) == 0 = (primeFactors (x:xs) (n `div` x) (ys ++ [x]))
    | otherwise = primeFactors xs n ys


primeFactorsFull :: [Integer] -> Integer -> [Integer] -> [Integer]
primeFactorsFull xs n [] = primeFactorsFull ys n ys
                           where ys = primeFactors xs n []
primeFactorsFull [] n ys = ys
primeFactorsFull xs n ys 
    | not $ y `elem` ys = ys ++ [y]
    | otherwise = ys 
      where y = n `div` (last xs)

(^!) :: Num a => a -> Int -> a
(^!) x n = x^n
 
squareRoot :: Integer -> Integer
squareRoot 0 = 0
squareRoot 1 = 1
squareRoot n =
   let twopows = iterate (^!2) 2
       (lowerRoot, lowerN) =
          last $ takeWhile ((n>=) . snd) $ zip (1:twopows) twopows
       newtonStep x = div (x + div n x) 2
       iters = iterate newtonStep (squareRoot (div n lowerN) * lowerRoot)
       isRoot r  =  r^!2 <= n && n < (r+1)^!2
   in  head $ dropWhile (not . isRoot) iters


--showFactors :: Integer -> [Integer]
--showFactors n = primeFactors (defaultPossiblePrimes $ (squareRoot n)) n []

--showFactorsS :: String -> String
--showFactorsS v = show (showFactors (read v::Integer))

--main :: IO()
--main = interact showFactorsS
--main = putStrLn (show (primeFactors (defaultPossiblePrimes $ squareRoot 600851475143) 600851475143 []))
main = putStrLn (show (primeFactorsFull (defaultPossiblePrimes $ squareRoot 15) 15 []))
