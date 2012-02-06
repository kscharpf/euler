mapMod2 :: Int -> Int
mapMod2 x
  | (mod x 2) == 0 = x
  | otherwise = 0

fibiter :: [Int] -> Int -> Int -> Int -> [Int]
fibiter xs a b 0 = xs
fibiter xs a b c = (fibiter (xs ++ [a]) (a + b) a (c-1))

-- sum (map mapMod2 (takeWhile (<4000000) (fibiter [] 1 0 4000000)))
