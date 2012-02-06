isMod35 :: Int -> Int
isMod35 x
  | (mod x 3 == 0) = x
  | (mod x 5 == 0) = x
  | otherwise = 0 

main :: IO()
main = put sum (filter isMod35 [1..1000])

